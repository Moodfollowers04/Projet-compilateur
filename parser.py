"""Partie 3 : Analyseur Syntaxique"""
from lexer import tokenize
class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
    def courant(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else ('EOF', '', -1)
    def accepter(self, attendu):
        kind, val, ligne = self.courant()
        if kind == attendu or val.lower() == attendu.lower():
            self.pos += 1
            return val
        raise SyntaxError(f"Attendu '{attendu}', trouvé '{val}' ligne {ligne}")
    def programme(self):
        self.accepter('programme')
        nom = self.accepter('IDENT')
        self.accepter(';')
        if self.courant()[1].lower() == 'var':
            self.declarations()
        self.accepter('debut')
        self.instructions()
        self.accepter('fin')
        self.accepter('.')
        print(f"OK : programme '{nom}' valide !")
    def declarations(self):
        self.accepter('var')
        self.accepter('IDENT')
        while self.courant()[1] == ',':
            self.accepter(',')
            self.accepter('IDENT')
        self.accepter(':')
        self.accepter('entier')
        self.accepter(';')
    def instructions(self):
        self.instruction()
        while self.courant()[1] == ';':
            self.accepter(';')
            if self.courant()[1].lower() not in ('fin', 'sinon'):
                self.instruction()
    def instruction(self):
        val = self.courant()[1].lower()
        if self.courant()[0] == 'IDENT':
            self.accepter('IDENT')
            self.accepter(':=')
            self.expression()
        elif val == 'lire':
            self.accepter('lire')
            self.accepter('(')
            self.accepter('IDENT')
            self.accepter(')')
        elif val == 'ecrire':
            self.accepter('ecrire')
            self.accepter('(')
            self.expression()
            self.accepter(')')
        elif val == 'si':
            self.accepter('si')
            self.condition()
            self.accepter('alors')
            self.instruction()
        elif val == 'tantque':
            self.accepter('tantque')
            self.condition()
            self.accepter('faire')
            self.instruction()
    def condition(self):
        self.expression()
        if self.courant()[1] in ('=', '<>', '<', '>', '<=', '>='):
            self.accepter('OPREL')
            self.expression()
    def expression(self):
        self.terme()
        while self.courant()[1] in ('+', '-'):
            self.accepter('OPARIT')
            self.terme()
    def terme(self):
        self.facteur()
        while self.courant()[1] in ('*', '/'):
            self.accepter('OPARIT')
            self.facteur()
    def facteur(self):
        kind, val, ligne = self.courant()
        if kind == 'NOMBRE':
            self.accepter('NOMBRE')
        elif kind == 'IDENT':
            self.accepter('IDENT')
        elif val == '(':
            self.accepter('(')
            self.expression()
            self.accepter(')')
if __name__ == "__main__":
    code = """
    programme test;
    var x : entier;
    debut
        lire(x);
        x := x + 1;
        ecrire(x)
    fin.  """
    tokens = tokenize(code)
    Parser(tokens).programme()