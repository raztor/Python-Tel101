from matplotlib import pyplot
import matplotlib.ticker as ticker


def temperaturas(nombre_archivo):
    anos = []
    temperaturas_total = []
    archivo = open(nombre_archivo, 'r', encoding='UTF8')

    for linea in archivo:
        ano, temperatura = linea.split(',')
        anos.append(ano)
        temperaturas_total.append(float(temperatura))

    archivo.close()

    '''Todo esto es una suposicion'''

    tick_spacing = 20
    fig, ax = pyplot.subplots(1, 1)
    ax.plot(anos, temperaturas_total)
    ax.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))

    '''Hasta acá'''

    pyplot.grid(color='gray', linestyle='dotted')
    pyplot.xlabel('Año')
    pyplot.ylabel('Temperatura (ºC)')
    pyplot.savefig('temperaturas.pdf')
    pyplot.show()

    return round(sum(temperaturas_total)/len(temperaturas_total), 2)


print(temperaturas("temperatures.txt"))
