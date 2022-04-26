import random
import math
print("Bienvenid@s al GimnasIWI!")
mc= int(input("Ingrese meta en calorias: "))
fin=0
totalcal=0
while fin==0:
    if mc<totalcal:
        print('************\nMeta cumplida! Quemaste', str(totalcal), 'de un total de', str(mc), 'calorias')
        fin=1
    else:
        repeticiones=0
        ejer=0
        numeroejercicio=int(input('Ingrese ejercicio\n(1) Sentadillas sumo\n(2) Plancha abdominal\n(3) Press frances\n(4) Me canse\n'))
        if numeroejercicio==1:
            nombreejercicio='SENTADILLAS SUMO'
        elif numeroejercicio==2:
            nombreejercicio='PLANCHA ABDOMINAL'
        elif numeroejercicio==3:
            nombreejercicio='PRESS FRANCES'
        elif numeroejercicio==4:
            print('************\nA descansar! Quemaste', str(totalcal), 'calorias')
            ejer=1
            fin=1
        else:
            print('Ingrese una opcion valida')
            ejer=1
        while ejer==0:
            print(nombreejercicio)
            if numeroejercicio==1:
                repeticiones=int(input('¿Cuantas repeticiones?: '))
                cal = random.randint(3, 7)
                caltot=repeticiones*cal
                print('Calorias quemadas con sentadillas: ',str(caltot))
                totalcal+=caltot
                print('Calorias hasta el momento: ', str(totalcal))
                ejer = 1
            elif numeroejercicio==2:
                sumat=1
                valsumat=0
                repeticiones = int(input('¿Cuantos segundos?: '))
                while sumat<repeticiones:
                    fact=1
                    valorfact=1
                    while fact<=sumat:
                        valorfact=valorfact*fact #esto da el total del factorial
                        fact=fact+1
                    valsumat=valsumat+((4**sumat)/valorfact)
                    sumat += 1
                totalcal+=round(valsumat)
                print('Calorias quemadas con sentadillas: ',str(round(valsumat)))
                print('Calorias hasta el momento: ', str(totalcal))
                ejer = 1
            elif numeroejercicio==3:
                repeticiones = int(input('¿Cuantas repeticiones?: '))
                peso= int(input('¿Cuantos Kilos?'))
                if repeticiones>=peso:
                    y=1
                    x=repeticiones
                    subtot=repeticiones
                    while y<peso:
                        x=1+math.sqrt(x)
                        subtot+=5
                        y+=1
                else:
                    y=1
                    x=peso
                    subtot=peso
                    while y<repeticiones:
                        x=1+math.sqrt(x)
                        subtot+=x
                        y+=1
                print('Calorias quemadas con press frances: ', round(subtot))
                totalcal+=round(subtot)
                print('Calorias hasta el momento: ', str(totalcal))
                ejer = 1