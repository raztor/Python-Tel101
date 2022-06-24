def notas(lista):
    dicc = {}
    for linea in lista:
        cancion, album, artistas, nota = linea
        for artista in artistas:
            if artista in dicc:
                dicc[artista].append(nota)
            else:
                dicc[artista] = [nota]

    return dicc


def hits(lista):
    dicc = {}
    promedios = notas(lista)
    for artista in promedios:
        promedios[artista] = round(sum(promedios[artista])/(len(promedios[artista])), 1)
    for linea in lista:
        cancion, album, artistas, nota = linea
        for artista in artistas:
            if nota > promedios[artista]:
                if artista in dicc:
                    dicc[artista] += 1
                else:
                    dicc[artista] = 1
            elif nota >= promedios[artista]:
                if artista not in dicc:
                    dicc[artista] = 0
    dicc = list(dicc.items())
    preordenado = []
    ordenado = []
    for item in dicc:
        artista, nota = item
        preordenado.append((nota, artista))
    preordenado.sort(reverse=True)

    for item in preordenado:
        nota, artista = item
        ordenado.append((artista, nota))

    return ordenado[:3]


lista = [('Hello', '25', ['Adele'], 4),
('La Bicicleta', 'El Dorado', ['Vives', 'Shakira'], 3),
('Trap', 'El Dorado', ['Shakira', 'Maluma'], 5),
('Hello', '25', ['Adele'], 5),
('Chantaje', 'El Dorado', ['Shakira', 'Maluma'], 5)]

'''Prints funcion Nº1'''
# print(notas(lista))

'''Prints funcion Nº2'''
print(hits(lista))
