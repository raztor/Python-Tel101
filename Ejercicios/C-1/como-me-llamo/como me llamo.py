cantidad=1
nombre=str(input('Nombre'))
input2=(input('Intento'))
while input2!=nombre:
    cantidad=cantidad+1
    input2=(input('Intento'))
else:
    print(cantidad)
