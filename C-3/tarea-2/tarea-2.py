#Codigo por raztorr
def reprobados(nombre_archivo, ano):
    txt = open(nombre_archivo, 'r', encoding='UTF8')
    newtxt = open(f'{ano}.txt', 'w', encoding='UTF8')
    newtxt.write(f'Alumnos reprobados el año {ano}\n')
    newtxt.close()
    contador = 0
    reprueban = []
    newtxt = open(f'{ano}.txt', 'a', encoding='UTF8')
    for linea in txt:
        nombre, ramo, año, motivo = linea.split(':')
        if int(año) == int(ano):
            newtxt.write(f'\t{nombre} va a reprobar {ramo}\n')
            reprueban.append(nombre)
            contador += 1
    newtxt.write(f'total de reprobados el año {ano}: {contador}')
    newtxt.close()
    txt.close()
    return reprueban

def alumnos(nombre_archivo):
    txt = open(nombre_archivo, 'r', encoding='UTF8')
    cantidadtot = 0
    for linea in txt:
        nombre, ramos = linea.split(':')
        ramos = ramos.split(',')
        newtxt = open(f'{nombre}.txt', 'w', encoding='UTF8')
        newtxt.write(f'Asignaturas reprobadas por {nombre}:')
        newtxt.close()
        cantidad = 0
        newtxt = open(f'{nombre}.txt', 'a', encoding='UTF8')
        for ramo in ramos:
            newtxt.write(f'\r\t{ramo}')
            cantidad += 1
        newtxt.write(f'Total de asignaturas reprobadas por {nombre}: {cantidad}')
        cantidadtot += 1
        newtxt.close()
    txt.close()
    return cantidadtot

print(reprobados("pag1.txt", 2020))
print(alumnos("Pyuk.txt"))