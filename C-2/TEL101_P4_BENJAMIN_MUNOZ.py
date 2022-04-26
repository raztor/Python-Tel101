import random
def moneda(r1, r2, r3, apuesta):
    if apuesta == r1 or apuesta == r2 or apuesta == r3:
        if r1 == r2 and r2 == r3:
            return 9
        elif r1 == r3:
            return 2
        elif r1 == r2 or r2 == r3:
            return 4
        else:
            return 1
    else:
        return 0
fin=0
while fin == 0:
    inicio = str(input('Desea apostar?: '))
    if inicio == 'NO':
        fin = 1
    else:
        apuesta=int(input('Ingrese número al cual le apuesta: '))
        r1 = (random.randint(1, 9))
        r2 = (random.randint(1, 9))
        r3 = (random.randint(1, 9))
        monedas=moneda(r1, r2, r3, apuesta)
        print(r1, r2, r3)
        print('Monedas: ', str(monedas))