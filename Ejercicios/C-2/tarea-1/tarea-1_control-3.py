###Codigo por Raztorr
def ventaja(vja):
    if vja=='agua':
        return 'fuego'
    if vja=='fuego':
        return 'planta'
    if vja=='planta':
        return 'agua'
def desventaja(dvja):
    if dvja=='agua':
        return 'planta'
    if dvja=='fuego':
        return'agua'
    if dvja=='planta':
        return 'fuego'
def efectiviad(t1,t2):
    if t2==ventaja(t1):
        return 2
    elif t2==desventaja(t1):
        return 0.5
    else:
        return 1
def ataque(fuerza,t1,t2):
    total=efectiviad(t1,t2)*fuerza
    return total
def duelo(pkm1, fuerza1, t1, pkm2, fuerza2, t2):
    attack1=fuerza1*efectiviad(t1,t2)
    attack2=fuerza2*efectiviad(t2,t1)
    if attack1>attack2:
        return pkm1
    elif attack1<attack2:
        return pkm2
    elif attack1==attack2:
        return 'Empate'

pkm1=str(input('Pokemon 1: '))
att1=float(input('Ataque Pokemon 1: '))
t1=str(input('Tipo Pokemon 1: '))
pkm2=str(input('Pokemon 2: '))
att2=float(input('Ataque Pokemon 2: '))
t2=str(input('Tipo Pokemon 2: '))

if duelo(pkm1, att1, t1, pkm2, att2, t2)=='Empate':
    print('Empate')
else:
    print('Gana ',duelo(pkm1, att1, t1, pkm2, att2, t2))