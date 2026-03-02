"""Compilateur complet : code et exécution"""
from lexer import tokenize
from codegen import Codegen
from mach import mach
def compiler(code_source):
    print(" Code source ")
    print(code_source)

    print("\n Analyse lexicale ")
    tokens = tokenize(code_source)

    print("\n Génération P-code ")
    pcode = Codegen(tokens).programme()
    for i, instr in enumerate(pcode):
        print(f"{i}: {instr}")

    print("\n Exécution du prog")
    mach(pcode)
if __name__ == "__main__":
    code = """
    programme essaie;
    var x, y, z : entier;
    debut
        lire(x);
        lire(y);
        z := x * y;
        ecrire(z)
    fin.
    """
    compiler(code)