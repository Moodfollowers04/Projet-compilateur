def mach(programme):
    pile = []
    memoire =  [0] * 100
    pc = 0
    while pc < len(programme):
        partie = programme[pc].split()
        inst = partie[0]
        arg = int (partie[1]) if len(partie) > 1 else None
        if inst == "LDI":
         pile.append(arg) #Pour empiler  LDI selon les instructions du TP

        elif inst == "STO": #stocke la valeur au sommet à l'adresse indiquée par le sous-sommet, dépile 2 fois
            memoire[arg] = pile.pop()

        elif inst == "LDV" :
            pile.append(memoire[arg])
        elif inst == "ADD":
            b = pile.pop()
            a = pile.pop()
            pile.append(a + b)
        elif inst == "SUB":
            b = pile.pop()
            a = pile.pop()
            pile.append(b - a)
        elif inst == "MUL":
            b = pile.pop()
            a = pile.pop()
            pile.append( a * b)
        elif inst == "DIV":
            b = pile.pop()
            a = pile.pop()
            pile.append(a // b)


        elif inst =="EQL":
            b = pile.pop()
            a = pile.pop()
            pile.append(1 if a==b else 0)
        elif inst == "NEQ":
            b = pile.pop()
            a = pile.pop()
            pile.append(1 if a != b else 0)
        elif inst == "GTR":
            a = pile.pop()
            b = pile.pop()
            pile.append(1 if a > b else 0)
        elif inst == "LSS":
            a = pile.pop()
            b = pile.pop()
            pile.append(1 if a<b else 0)
        elif inst == "GEQ":
            a = pile.pop()
            b = pile.pop()
            pile.append(1 if a>=b else 0)
        elif inst =="LEQ":
            a = pile.pop()
            b= pile.pop()
            pile.append(1 if a <= b else 0)

            #  Branchements (sauts)
        elif inst == "BRN":
            pc = arg
            continue  # On ne fait PAS pc += 1

        elif inst == "BZE":  # saut SI le sommet == 0
            val = pile.pop()
            if val == 0:
                pc = arg
                continue

        # entrée / sortie
        elif inst == "PRN":  # Affiche le sommet
            print(pile.pop())

        elif inst == "INN":
            memoire[arg] = int(input("? "))
        elif inst == "HLT":  # Arrête le programme
            break
        pc += 1