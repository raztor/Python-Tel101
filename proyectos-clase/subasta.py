#Codigo creado por Raztorr
inicio = str(input('Desea realizar una subasta?: '))

actual=0
total=0
totalsub=0
while inicio!='NO':
    nombre = str(input('Ingrese el nombre del producto: '))
    subastatotal = int(input('Ingrese la cantidad de ofertas permitidas: '))
    subasta = 0
    omayor = -1
    while subasta<subastatotal:
        subasta=subasta+1
        oactual=int(input('Ingrese la oferta:'))
        if oactual>omayor:
            omayor=oactual
        total=total+oactual
        totalsub=totalsub+1
    print(nombre+'vendido por $ '+str(omayor))
    inicio = str(input('Desea realizar una subasta?: '))
else:
    print('Se subastaron '+str(totalsub)+' productos')
    print('Recaudación total: $ '+str(total))