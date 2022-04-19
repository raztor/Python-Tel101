def puntos(car):
    if car=='inteligente':
        return 4
    elif car=='valiente':
        return 3
    elif car=='leal':
        return 2
    elif car=='responsable':
        return 1
    else:
        return 0
def nivel(lista):
    suma=0
    for car in lista:
        suma+=puntos(car)
    return suma
def disney(n1,l1,n2,l2):
    nivel1=nivel(l1)
    nivel2=nivel(l2)
    if nivel1>nivel2:
        return n1
    elif nivel1<nivel2:
        return n2
    else:
        return 'Empate'