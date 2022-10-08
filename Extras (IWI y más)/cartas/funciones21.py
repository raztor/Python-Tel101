import random
def generar_mazo():
    mazo = []
    cartas = list(range(2,11))+["A","J","Q","K"]
    HEARTS   = chr(9829)
    DIAMONDS = chr(9830)
    SPADES   = chr(9824)
    CLUBS    = chr(9827)
    pintas = [HEARTS, DIAMONDS, SPADES, CLUBS]
    for p in pintas:
        for c in cartas:
            mazo.append(str(c)+p)
    random.shuffle(mazo)
    return ver_cartas(mazo)

def eliminar_primera_carta(mazo):
    lista = mazo.split("-")
    return ver_cartas(lista[1:])

def ver_cartas(mano):
    r = "-".join(mano)
    return r