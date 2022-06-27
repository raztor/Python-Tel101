import matplotlib.pyplot as pp
import matplotlib.ticker as ticker

def poblacion_paises(nombre_archivo, region):
    paises_total = []
    total = {}
    archivo = open(nombre_archivo, 'r', encoding='UTF8')
    for linea in archivo:
        ano, pais, poblacion, zona = linea.rstrip().split(',')
        poblacion = int(poblacion)
        if zona == region:

            if pais in total:
                total[pais].append((ano, poblacion))
            else:
                total[pais] = [(ano, poblacion)]

            if pais not in paises_total:
                paises_total.append(pais)
    archivo.close()
    fig, ax = pp.subplots(1, 1)
    for item in total:
        anos_total = []
        poblacion_total = []
        total[item].sort()
        for algo in total[item]:
            year, pop = algo
            anos_total.append(year)
            poblacion_total.append(pop)
        ax.plot(anos_total, poblacion_total)


    ax.xaxis.set_major_locator(ticker.AutoLocator())
    ax.xaxis.set_minor_locator(ticker.AutoLocator())
    pp.xlabel("Eje x")
    pp.ylabel("Eje y")
    pp.show()


    return paises_total


print(poblacion_paises("paises.txt", "Latin America"))
