def tabla(resultados):
    favor = {}
    contra = {}
    difgol = {}
    pntpp = {}
    paises = []
    listafin = []
    lreordenada = []

    '''Esto crea diccionarios para con key de los paises para cuando luego le sume el valor a cada uno
     evitar un Key Error cuando el diccionario no esta creado'''

    for item in resultados:
        pais1, pais2 = item
        pntpp[pais1] = 0
        pntpp[pais2] = 0
        favor[pais1] = 0
        favor[pais2] = 0
        contra[pais1] = 0
        contra[pais2] = 0

    for item in resultados:

        pais1, pais2 = item
        rpais1, rpais2 = resultados[item]

        if rpais1 > rpais2:
            pntpp[pais1] += 3
        elif rpais1 < rpais2:
            pntpp[pais2] += 3
        elif rpais1 == rpais2:
            pntpp[pais1] += 1
            pntpp[pais2] += 1


        if not pais1 in paises:
            paises.append(pais1)

        if not pais2 in paises:
            paises.append(pais2)

        favor[pais1] += rpais1
        contra[pais1] += rpais2

        favor[pais2] += rpais2
        contra[pais2] += rpais1



    #print(*totgol.items(), sep='\n')

    for pais in paises:
        difgol[pais] = favor[pais] - contra[pais]

    '''Crea la lista (puntos, diferencia, pais) final antes de hacer sort'''


    for pais in paises:
        punto = pntpp[pais]
        difer = difgol[pais]
        listafin.append((punto, difer, pais))

    listafin.sort(reverse=True)

    '''
    reordena la lista de formato punto, difererencia, pais >>>>> pais, punto, diferencia
    '''

    for reordena in listafin:

        punto, difer, pais = reordena
        lreordenada.append((pais, punto, difer))

    return lreordenada

print(tabla({('Brasil', 'Venezuela'): (3, 0), ('Colombia', 'Ecuador'): (1, 0), ('Argentina', 'Chile'): (1, 1), ('Paraguay', 'Bolivia'): (3, 1), ('Colombia', 'Venezuela'): (0, 0), ('Brasil', 'Peru'): (4, 0)}))


