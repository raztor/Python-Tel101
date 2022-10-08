##programa por Raztor
##************CODIGO NO FINALIZADO*******************##
gananciatot=0
cantidaddeweas=0
Tru=1
while Tru==1: #no me dejaron usar un while True

    inicio = str(input('Desea realizar una mezcla?: '))
    if inicio=='SI':
        c = 0
        valc = 100
        h = 0
        valh = 200
        n = 0
        valn = 300
        cantiact=0
        valortot = 0
        cantitot=int(input('Ingrese la cantidad de elementos: '))
        cantidaddeweas=cantidaddeweas+1
        while cantiact<cantitot:
            cantiact=cantiact+1
            elemento=str(input('Ingrese un elemento: '))
            if elemento=='C':
                c=c+1
            elif elemento=='H':
                h=h+1
            elif elemento=='N':
                n=n+1
        valortot=c*valc+h*valh+n*valn
        gananciatot=gananciatot+valortot
        print('El valor de la mezcla C '+str(c)+' H '+str(h)+' N '+str(n)+' es: '+str(valortot))

    elif inicio=='NO':
        print('Cantidad de mezclas realizadas: '+str(cantidaddeweas))
        print('Ganancias totales: '+ str(gananciatot))
    Tru=0
