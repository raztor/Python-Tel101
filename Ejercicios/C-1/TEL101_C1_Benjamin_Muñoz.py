##codigo por Raztorr
##************************CODIGO NO FINALIZADO***********************************
qtyparticipantes=int(input('Ingrese la cantidad de participantes: '))
numeroparticipante=0
totallanza=0
ganador='N/A'
distmax=0
while qtyparticipantes>numeroparticipante:
    distancia=0
    print()
    print('Participante '+ str(numeroparticipante+1))
    numeroparticipante=numeroparticipante+1
    nombre=str(input('Ingrese el nombre del participante: '))
    promedio=0
    intento=1
    contdist = 0
    while distancia>-1:
        contdist=contdist+distancia
        promedio = (contdist/intento)
        distancia=float(input('Ingrese la distancia: '))
        intento=intento+1

    print('El promedio de '+nombre+' es '+str(promedio))
print('Total de lanzamientos vàlidos: ' + str(totallanza))
print('El participante ganador es '+ganador+ ' con una distancia de '+ str(distmax))