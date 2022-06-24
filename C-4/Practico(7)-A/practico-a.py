def f1(especie, lista):
    dicc = {}
    for item in lista:
        fecha, ciudad, especies = item
        if especie in especies:
            if ciudad in dicc:
                dicc[ciudad] += 1
            else:
                dicc[ciudad] = 1
    return dicc


def f2(lista):
    dicc = {}
    for item in lista:
        fecha, ciudad, especies = item
        for especie in especies:
            if especie in dicc:
                if ciudad in dicc[especie]:
                    dicc[especie] = dicc[especie]
                else:
                    dicc[especie].append(ciudad)
            else:
                dicc[especie] = [ciudad]
    return dicc

observaciones = [('2019/12/17', 'Valparaiso', ['Chercan', 'Cormoran']),
('2019/12/15', 'Santiago', ['Zorzal', 'Paloma', 'Chercan']),
('2019/12/19', 'Valparaiso', ['Gaviota', 'Colibri']),
('2019/12/20', 'Santiago', ['Chercan', 'Loica', 'Paloma']),
('2019/12/14', 'Curico', ['Loica', 'Queltehue', 'Pelicano', 'Colibri']),
('2019/12/17', 'Santiago', ['Cisne', 'Colibri', 'Chercan']),
('2019/12/15', 'Curico', ['Colibri', 'Loica'])]

'''Prints funcion Nº1'''
# print(f1("Colibri", observaciones))

'''Prints funcion Nº2'''
# print(f2(observaciones))
