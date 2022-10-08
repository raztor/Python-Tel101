cantidad=0
fin=0
while fin!=1:
    barney=int(input('Nùmero Barney'))
    oponente= int(input('Número oponente'))
    cantidad=cantidad+1
    if barney==oponente:
        resultado='Empate'
        fin=1
    elif barney>oponente:
        resultado='Victoria'
        fin=1
else:
    print(cantidad)
    print(resultado)
