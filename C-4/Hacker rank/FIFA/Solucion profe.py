def tabla(resultados):
    totgol = {}
    difgol = {}
    puntos = {}
    paises = []
    listafin = []
    lreordenada = []

    for item in resultados:
        pais1, pais2 = item
        rpais1, rpais2 = resultados[item]

        if not pais1 in paises:
            paises.append(pais1)

        if not pais2 in paises:
            paises.append(pais2)

        '''
        Comienza el codigo de los puntajes
        '''

        if pais1 not in puntos:
            puntos[pais1] = 0

        if pais2 not in puntos:
            puntos[pais2] = 0

        if rpais1 > rpais2:

            oldval1 = puntos[pais1]
            puntos[pais1] = oldval1 + 3


        elif rpais1 < rpais2:

            oldval2 = puntos[pais2]
            puntos[pais2] = oldval2 + 3


        elif rpais1 == rpais2:

            oldval1 = puntos[pais1]
            oldval2 = puntos[pais2]
            puntos[pais1] = oldval1 + 1
            puntos[pais2] = oldval2 + 1

        if pais1 in totgol:
            oldval = totgol[pais1]
            favor, contra = oldval
            totgol[pais1] = (favor + rpais1, contra + rpais2)
        else:
            totgol[pais1] = (rpais1, rpais2)

        if pais2 in totgol:
            oldval = totgol[pais2]
            favor, contra = oldval
            totgol[pais2] = (favor + rpais2, contra + rpais1)
        else:
            totgol[pais2] = (rpais2, rpais1)

    for pais in totgol:
        favor, contra = totgol[pais]
        difgol[pais] = favor - contra

    '''Crea la lista (puntos, diferencia, pais) final antes de hacer sort'''

    for pais in paises:
        if pais in puntos:
            punto = puntos[pais]
        else:
            punto = 0

        difer = difgol[pais]
        listafin.append((punto, difer, pais))

    listafin.sort(reverse=True)

    '''
    reordena la lista de formato punto, difererencia, pais >>>>> pais, punto, diferencia
    '''

    for reordena in listafin:
        punto, difer, pais = reordena
        lreordenada.append((pais, punto, difer))
    # print(totgol['Brasil'])

    return lreordenada


# Esto se usa para ejecutar y cambiar los datos
print(tabla({('Brasil', 'Venezuela'): (3, 0), ('Colombia', 'Ecuador'): (1, 0), ('Argentina', 'Chile'): (1, 1), ('Paraguay', 'Bolivia'): (3, 1), ('Colombia', 'Venezuela'): (0, 0), ('Brasil', 'Peru'): (4, 0)}))