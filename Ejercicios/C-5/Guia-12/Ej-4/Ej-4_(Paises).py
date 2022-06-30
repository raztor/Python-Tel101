import matplotlib.pyplot as pp

def poblacion_paises(nombre_archivo, region):
    total = {}
    tot_paises = []
    archivo = open(nombre_archivo, 'r', encoding='UTF8')
    for linea in archivo:
        ano, pais, poblacion, zona = linea.strip().split(',')
        poblacion = int(poblacion)
        ano = int(ano)
        if zona == region:
            if pais not in total:
                total[pais] = []
                total[pais].append((ano, poblacion))

    archivo.close()

    for pais_for in total:
        tot_paises.append(pais_for)
        total[pais_for].sort()
        x = []
        y = []
        for ano_algo, poblacion_total in total[pais_for]:
            x.append(ano_algo)
            y.append(poblacion_total)
        pp.plot(x,y,label=pais_for)

    pp.legend()
    pp.show()


    return tot_paises


print(poblacion_paises("paises.txt", "Latin America"))
