cantest = int(input('Ingrese la cantidad de estudiantes: '))
print('')
cantact = 0
add = ''

while cantact < cantest:
    cantact += 1
    estact = str(input(f'Ingrese Nombre y Apellido de estudiante {cantact}: '))
    notasact = str(input(f'Ingrese las Notas de estudiante {cantact}: '))
    print('')
    add += (f'{estact}|{notasact}:')

add = add.split(':')
add.remove('')

for alumno in add:
    nombre, nota = alumno.split('|')
    nombre, apellido = nombre.split(' ')
    nota = (nota.split(','))
    nota = [float(i) for i in nota]
    print(f'El promedio de {nombre} es {round(sum(nota)/len(nota), 2)}')