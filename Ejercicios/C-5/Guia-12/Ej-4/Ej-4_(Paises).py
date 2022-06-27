import matplotlib.pyplot as pp
import matplotlib.ticker as ticker

def poblacion_paises(nombre_archivo, region):
    paises_total = []
    total = {}
    fechas = {}
    pobla = {}
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
    for item in total:
        total[item].sort()
    for country in total:
        for linea in total[country]:
            date, pop = linea
            if country in fechas:
                fechas[country].append(date)
                pobla[country].append(pop)
            else:
                fechas[country] = [date]
                pobla[country] = [pop]

    fig, ax = pp.subplots(1, 1)
    for item in reversed(paises_total):
        print(pobla[item])
        ax.plot(fechas[item], pobla[item])

    '''Use esto, ya que se me ploteaban todos los años en el eje y no se leia nada'''
    ax.xaxis.set_major_locator(ticker.AutoLocator())
    ax.xaxis.set_minor_locator(ticker.AutoLocator())

    pp.xlabel("Eje x")
    pp.ylabel("Eje y")
    pp.show()


    return paises_total


print(poblacion_paises("paises.txt", "Latin America"))
