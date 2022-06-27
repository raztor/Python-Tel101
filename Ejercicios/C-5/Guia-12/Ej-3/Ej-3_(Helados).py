import matplotlib.pyplot as pp


def f1(nombre_archivo, ciudad):
    dicc = {}
    sabores = []
    cantidades = []
    archivo = open(nombre_archivo, 'r', encoding='UTF8')
    for linea in archivo:
        linea = linea.rstrip()
        _, city, sabor = linea.split(';')
        if ciudad == city:
            sabor = sabor.split(',')
            for item in sabor:
                if item in dicc:
                    dicc[item] += 1
                else:
                    dicc[item] = 1
    archivo.close()
    for item in dicc:
        sabor = item
        cantidad = dicc[item]
        sabores.append(sabor)
        cantidades.append(cantidad)

    pp.figure(dpi=100)
    pp.title(f'Preferencias de sabores en {ciudad}')
    pp.pie(cantidades, labels=sabores, autopct="%.2f%%")
    pp.savefig(f'{ciudad}.pdf')
    pp.show()

    return max(dicc, key=dicc.get)


def f2(nombre_archivo, sabor):
    dicc = {}
    lista = []
    lista_return = []
    ciudades = []
    cantidades = []
    archivo = open(nombre_archivo, 'r', encoding='UTF8')
    for linea in archivo:
        _, city, sabores = linea.split(';')
        if sabor in sabores:
            if city in dicc:
                dicc[city] += 1
            else:
                dicc[city] = 1
    archivo.close()
    for item in dicc:
        ciudad = item
        cantidad = dicc[ciudad]
        lista.append((cantidad, ciudad))
        ciudades.append(ciudad)
        cantidades.append(cantidad)

    lista.sort(reverse=True)

    cont = 0
    for item in lista:
        cont += 1
        cantidad, ciudad = item
        lista_return.append(ciudad)

    pp.bar(ciudades, cantidades)
    pp.title(f'Preferencias por ciudad de sabor {sabor}')
    pp.savefig(f'{sabor}.pdf')
    pp.show()

    return lista_return


'''Prints Funcion Nº1'''
# print(f1("helados.txt", "Santiago"))

'''Prints Funcion Nº2'''
# print(f2("helados.txt", "Vainilla"))
