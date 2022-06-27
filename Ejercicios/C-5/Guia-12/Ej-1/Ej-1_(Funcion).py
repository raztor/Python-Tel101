""" Ya que el grafico entrega los valores desordenados en la lista
    a pesar de que no esta en las instrucciones para que de
    correctamente primero se debe hacer un sort """

from matplotlib import pyplot


def altura(lista):
    y = []
    lista.sort()
    for item in lista:
        y.append((-5*item**2+120*item))
    print(y)
    pyplot.xlabel("Eje x")
    pyplot.ylabel("Eje y")
    pyplot.plot(lista, y, 'g-o')
    pyplot.grid(color='gray', linestyle='--', linewidth=0.2)
    pyplot.show()

    return max(y)


print(altura([0.5, 12, 26, 25, 20, 18, 14, 12, 8, 6, 5, 3]))
