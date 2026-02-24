"""Partie 2 : Analyseur Lexical"""
import re
TOKENS = [
    ('MOTCLE',    r'\b(programme|var|debut|fin|si|alors|sinon|tantque|faire|lire|ecrire|entier)\b'),
    ('NOMBRE',    r'\d+'),
    ('IDENT',     r'[a-zA-Z_]\w*'),
    ('AFFECT',    r':='),
    ('OPREL',     r'<=|>=|<>|<|>|='),
    ('OPARIT',    r'[+\-*/]'),
    ('DELIM',     r'[();,:.]'),
    ('NEWLINE',   r'\n'),
    ('SKIP',      r'[ \t]+'),
    ('COMMENT',   r'\{[^}]*\}'),
    ('ERREUR',    r'.'),]
regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in TOKENS)
def tokenize(code):
    tokens = []
    ligne = 1
    for m in re.finditer(regex, code, re.IGNORECASE):
        kind = m.lastgroup
        value = m.group()
        if kind == 'NEWLINE':
            ligne += 1
        elif kind in ('SKIP', 'COMMENT'):
            continue
        elif kind == 'ERREUR':
            raise SyntaxError(f"Caractère invalide '{value}' ligne {ligne}")
        else:
            tokens.append((kind, value, ligne))
    return tokens
if __name__ == "__main__":
    code = """
    programme test;
    var x : entier;
    debut
        lire(x);
        x := x + 1;
        ecrire(x)
    fin.
    """
    for tok in tokenize(code):
        print(tok)