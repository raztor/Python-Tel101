# Completar esto solamente
def resumen(datos, notas, paralelo):
    nn = []
    aprobados = []
    reprobados = []
    sorter = []
    cont = 0
    for dato in datos:
        nombre, rol, paral = dato
        if paral == paralelo:
            for info in notas:
                if info[0] == rol:
                    nn.append((nombre, info[1]))

    for elemento in nn:
        nombre, notas = elemento
        notas = list(notas)
        promedio = sum(notas) / len(notas)
        sorter.append((promedio, nombre))

    sorter.sort()

    for y in sorter:
        promedio, nombre = y
        if promedio >= 55:
            aprobados.append(nombre)
        elif promedio < 55:
            reprobados.append(nombre)

    return (reprobados, aprobados)


# Esto se usa para ejecutar y cambiar los datos
print(resumen(eval(input()), eval(input()), int(input())))