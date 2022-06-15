'''ESTE CODIGO CONTIENE ERRORES Y NO FUNCIONA PARA TODOS LOS CASOS'''
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

        if rpais1 > rpais2:

            ''' De aqui hacia abajo uso el try para intentar ver si hay un valor antiguo y en caso de que no 
            exista un valor guardado en el diccionario para esa llave, entonces se crea el valor con el except'''

            try:
                oldval1 = puntos[pais1]
                puntos[pais1] = oldval1 + 3
            except:

                puntos[pais1] = 3

        elif rpais1 < rpais2:
            try:
                oldval2 = puntos[pais2]
                puntos[pais2] = oldval2 + 3
            except:

                puntos[pais2] = 3

        elif rpais1 == rpais2:
            try:
                oldval1 = puntos[pais1]
                oldval2 = puntos[pais2]
                puntos[pais1] = oldval1 + 1
                puntos[pais2] = oldval2 + 1

            except:

                puntos[pais1] = 1
                puntos[pais2] = 1

        try:
            oldval = totgol[pais1]
            # print(*totgol.items(), sep='\n')
            favor, contra = oldval
            totgol[pais1] = (favor + rpais1, contra + rpais2)

            oldval = totgol[pais2]
            favor, contra = oldval
            totgol[pais2] = (favor + rpais2, contra + rpais1)
        except:

            totgol[pais1] = (rpais1, rpais2)
            totgol[pais2] = (rpais2, rpais1)

    # print(*totgol.items(), sep='\n')

    for pais in totgol:
        favor, contra = totgol[pais]
        difgol[pais] = favor - contra

    '''Crea la lista (puntos, diferencia, pais) final antes de hacer sort'''

    for pais in paises:
        try:
            punto = puntos[pais]
        except:
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


print(tabla({('Brasil', 'Venezuela'): (3, 0), ('Colombia', 'Ecuador'): (1, 0), ('Argentina', 'Chile'): (1, 1),
             ('Paraguay', 'Bolivia'): (3, 1), ('Colombia', 'Venezuela'): (0, 0), ('Brasil', 'Peru'): (4, 0)}))
