qtydistritos=int(input('Ingrese la cantidad de distritos: '))
A=0
B=0
C=0
Atot=0
Btot=0
Ctot=0
numerodistrito=0

while qtydistritos>numerodistrito:
    print()
    print('Distrito '+ str(numerodistrito+1))
    A = 0
    B = 0
    C = 0
    numerodistrito=numerodistrito+1
    qtyvotantes=int(input('Ingrese la cantidad de votantes: '))
    votantes=0
    while qtyvotantes>votantes:
        votantes=votantes+1
        voto=str(input('Ingrese su voto: '))
        if voto=='A':
            A=A+1
            Atot=Atot+1
        elif voto=='B':
            B=B+1
            Btot=Btot+1
        elif voto=='C':
            C=C+1
            Ctot=Ctot+1

total=Atot+Btot+Ctot
print()
print('Resultados Votaciones')
print('Total A: '+str(Atot)+' votos ( '+str(Atot/total*100)+' % )')
print('Total B: '+str(Btot)+' votos ( '+str(Btot/total*100)+' % )')
print('Total C: '+str(Ctot)+' votos ( '+str(Ctot/total*100)+' % )')

if Atot>Btot and Atot>Ctot: #Gana A
    print('Ganador: A')
elif Btot>Atot  and Btot>Ctot: #Gama B
    print('Ganador: B')
elif Ctot>Atot and Ctot>Btot: #Gana C
    print('Ganador: C')
elif Ctot==Atot and Atot==Btot: #empate
    print('Empate: A, B y C')
elif Atot==Btot: #empata A y B
    print('Empate: A y B')
elif Atot==Ctot: #empate A y C
    print('Empate: A y C')
elif Btot==Ctot: #empate B y C
    print('Empate: B y C')













##codigo por Raztorr
qtyparticipantes=int(input('Ingrese la cantidad de participantes: '))
numeroparticipante=0
totallanza=0
ganador='N/A'
distmax=0
contdist=0
while qtyparticipantes>numeroparticipante:
    distancia=0
    print()
    print('Participante '+ str(numeroparticipante+1))
    numeroparticipante=numeroparticipante+1
    nombre=str(input('Ingrese el nombre del participante: '))
    promedio=0
    intento=0
    while distancia>-1:
        if intento>=1:
            promedio = ((float(promedio) + float(distancia)) / 2)
        distancia=float(input('Ingrese la distancia: '))
        if intento==0:
            promedio=distancia
        intento=intento+1

    print('El promedio de '+nombre+' es '+str(promedio))
print('Total de lanzamientos vàlidos: ' + str(totallanza))
print('El participante ganador es '+ganador+ ' con una distancia de '+ str(distmax))