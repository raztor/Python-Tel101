# A python blackjack game
from funciones21 import *
def obtener_valor(mazo, usa_ases):
    valor = 0
    for carta in mazo.split("-"):
        if carta[0] in "JQK":
            valor += 10
        elif carta[0] == "A":
            if usa_ases==0:
                valor += 11
            else:
                valor += 1
        else:
            valor += int(carta[0])
    return (valor)
def leer_primera_carta(mazo):
    return mazo.split("-")[0]

mazo1 = generar_mazo()
nombre = input("¿Cuál es tu nombre? ")
mano_inicial = leer_primera_carta(mazo1)
mazo1 = eliminar_primera_carta(mazo1)
mano_inicial += "-" + leer_primera_carta(mazo1)
mazo1 = eliminar_primera_carta(mazo1)
print("Mano inicial", nombre, ":", mano_inicial)
mano_kiwi = leer_primera_carta(mazo1)
mazo1 = eliminar_primera_carta(mazo1)
print("Mano inicial Kiwi:", mano_kiwi)
terminar=0
if obtener_valor(mano_inicial,0)<21:
    as_usado_pers=0
else:
    as_usado_pers=1
if obtener_valor(mano_kiwi,0)<21:
    as_usado_kiwi=0
else:
    as_usado_kiwi=1

while (terminar != 1):
    print("Turno ", nombre)
    print("Tus cartas: ", mano_inicial)
    if obtener_valor(mano_inicial, as_usado_pers) > 21:
        as_usado_pers = 1
    else:
        as_usado_pers = 0
    if obtener_valor(mano_kiwi, as_usado_kiwi) > 21:
        as_usado_kiwi = 1
    else:
        as_usado_kiwi = 0
        
    print("Valor mano: ", obtener_valor(mano_inicial, as_usado_pers))
    sel = int(input("(1) Pedir carta \n(2) Pasar "))
    if sel == 1:
        mano_inicial += "-" + leer_primera_carta(mazo1)
        mazo1 = eliminar_primera_carta(mazo1)
        if obtener_valor(mano_inicial, as_usado_pers) > 21:
            print("Tus cartas: ",mano_inicial)
            print("Valor mano: ", obtener_valor(mano_inicial, as_usado_pers))
            print("Gana Kiwi. ",nombre, " pierde.")
            terminar = 1
        elif obtener_valor(mano_inicial, as_usado_pers) == 21:
            print("Tus cartas: ", mano_inicial)
            print("Valor mano: ", obtener_valor(mano_inicial, as_usado_pers))
            print("Gana ",nombre, ". Kiwi pierde.")
            terminar = 1
    else:
        print("Turno Kiwi")
        print("Cartas Kiwi: ", mano_kiwi)
        while obtener_valor(mano_inicial, as_usado_kiwi) < obtener_valor(mano_inicial, as_usado_pers):
            mano_kiwi += "-" + leer_primera_carta(mazo1)
            mazo1 = eliminar_primera_carta(mazo1)
            print("Cartas Kiwi: ", mano_kiwi)
            print("Valor mano Kiwi: ", obtener_valor(mano_inicial, as_usado_kiwi))
        if obtener_valor(mano_inicial, as_usado_kiwi) > 21:
            print("Gana ",nombre, ". Kiwi pierde.")
            terminar = 1
        elif obtener_valor(mano_inicial, as_usado_kiwi) > obtener_valor(mano_inicial, as_usado_pers):
            print("Gana Kiwi. ",nombre, " pierde.")
            terminar = 1
        else:
            print("Gana ",nombre,". Kiwi pierde.")
            terminar = 1