aforo=int(input('Aforo'))
prohibido=str(input('persona prohibida'))
cantidad=0
while cantidad<aforo:
    nombre=str(input('Nombre'))
    if nombre!=prohibido:
        cantidad=cantidad+1
        print('Bienvenid@ '+nombre+' '+str(cantidad)+' '+'/'+' '+str(aforo))

    else:
        print('No se admiten'+' '+prohibido)