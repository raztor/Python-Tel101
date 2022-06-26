def f1(pais, lista):
    dicc = {}
    for item in lista:
        ano, country, lugares = item
        if country == pais:
            for lugar in lugares:
                if lugar in dicc:
                    dicc[lugar] += 1
                else:
                    dicc[lugar] = 1
    return dicc


def f2(lista):
    dicc = {}
    for linea in lista:
        ano, country, lugares = linea
        if country in dicc:
            for lugar in lugares:
                if lugar in dicc[country]:
                    # pass
                    dicc[country] = dicc[country]
                else:
                    dicc[country].append(lugar)
        else:
            dicc[country] = []
            for lugar in lugares:
                dicc[country].append(lugar)

    return dicc

visitas = [(2010, 'Chile', ['Pomaire', 'Rapa Nui']),
(2012, 'EE.UU.', ['Golden Gate', 'Disneyland', 'Hollywood']),
(2012, 'Chile', ['Huilo Huilo', 'Pomaire']),
(2014, 'EE.UU.', ['Disneyland', 'Grand Canyon', 'Yellowstone']),
(2015, 'Italia', ['Fontana di Trevi', 'Pisa', 'Vaticano', 'Coliseo']),
(2016, 'EE.UU.', ['Grand Canyon', 'Disneyland', 'Hollywood']),
(2019, 'Italia', ['Coliseo', 'lago di Como'])]

'''Prints de la funcion Nº1'''
# print(f1("Italia", visitas))
# print(f1("EE.UU.", visitas))

'''Prints de la funcion Nº2'''

print(f2(visitas))
