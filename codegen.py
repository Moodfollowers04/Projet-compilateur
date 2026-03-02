"""Partie 4 : Générateur de P-code"""
from lexer import tokenize
class Codegen:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
        self.code = []
        self.vars = {}
        self.nvar = 0
    def courant(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else ('EOF', '', -1)

    def accepter(self, attendu):
        kind, val, _ = self.courant()
        if kind == attendu or val.lower() == attendu.lower():
            self.pos += 1
            return val
        raise SyntaxError(f"Erreur: attendu '{attendu}', trouvé '{val}'")

    def addr(self, nom):
        if nom not in self.vars:
            self.vars[nom] = self.nvar
            self.nvar += 1
        return self.vars[nom]

    def programme(self):
        self.accepter('programme')
        self.accepter('IDENT')
        self.accepter(';')
        if self.courant()[1].lower() == 'var':
            self.declarations()
        self.accepter('debut')
        self.instructions()
        self.accepter('fin')
        self.accepter('.')
        self.code.append('HLT')
        return self.code

    def declarations(self):
        self.accepter('var')
        self.addr(self.accepter('IDENT'))
        while self.courant()[1] == ',':
            self.accepter(',')
            self.addr(self.accepter('IDENT'))
        self.accepter(':')
        self.accepter('entier')
        self.accepter(';')

    def instructions(self):
        self.instruction()
        while self.courant()[1] == ';':
            self.accepter(';')
            if self.courant()[1].lower() not in ('fin',):
                self.instruction()

    def instruction(self):
        kind, val, _ = self.courant()
        if kind == 'IDENT':
            nom = self.accepter('IDENT')
            self.accepter(':=')
            self.expression()
            self.code.append(f"STO {self.addr(nom)}")
        elif val.lower() == 'lire':
            self.accepter('lire')
            self.accepter('(')
            nom = self.accepter('IDENT')
            self.accepter(')')
            self.code.append(f"INN {self.addr(nom)}")
        elif val.lower() == 'ecrire':
            self.accepter('ecrire')
            self.accepter('(')
            self.expression()
            self.accepter(')')
            self.code.append('PRN')

    def expression(self):
        self.terme()
        while self.courant()[1] in ('+', '-'):
            op = self.accepter('OPARIT')
            self.terme()
            self.code.append('ADD' if op == '+' else 'SUB')

    def terme(self):
        self.facteur()
        while self.courant()[1] in ('*', '/'):
            op = self.accepter('OPARIT')
            self.facteur()
            self.code.append('MUL' if op == '*' else 'DIV')

    def facteur(self):
        kind, val, _ = self.courant()
        if kind == 'NOMBRE':
            self.accepter('NOMBRE')
            self.code.append(f"LDI {val}")
        elif kind == 'IDENT':
            nom = self.accepter('IDENT')
            self.code.append(f"LDV {self.addr(nom)}")

    def get_var_names(self):
        return {v: k for k, v in self.vars.items()}

if __name__ == "__main__":
    code = """
    programme test;
    var x : entier;
    debut
        lire(x);
        x := x + 5;
        ecrire(x)
    fin.
    """
    tokens = tokenize(code)
    pcode = Codegen(tokens).programme()
    for i, instr in enumerate(pcode):
        print(f"{i}: {instr}")