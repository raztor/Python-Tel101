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
#def duelo(pkm1, fuerza1, t1, pkm2, fuerza2, t2):
