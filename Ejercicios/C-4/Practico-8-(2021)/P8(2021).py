lista = [
('Rapida', 'McDolars', 3807),
('China', 'Fu King Chinese', 1874),
('Mariscos', 'Frying Nemo', 2740),
('Rapida', 'Hungry Birds', 894),
('Rapida', 'Churrasic Park', 2427),
('Thai', 'Dalai Lomo', 404),
('China', 'Kung Food', 989),
('Rapida', 'Marco Pollo', 1004),
('Mariscos', 'La Concha de tu Mar', 1411),
('Sangucheria', 'Bread Pitt', 1140),
('China', 'Niu Na Hua', 5790),
('Italiana', 'TerePizza', 2215),
('Sangucheria', 'Paul MasCarney', 150),
('Vegana', 'No vives de ensalada', 1101),
('Italiana', 'Torre di pizza', 1689),
('Italiana', 'Massa para la mesa', 1534),
('Restobar', 'Alcoholegio', 1347)]


def pedidos(lista):
    dicc = {}
    for linea in lista:
        tipo, nombre, total = linea
        if tipo in dicc:
            dicc[tipo] += total
        else:
            dicc[tipo] = total
    return dicc


def tipos(lista):
    llarga = []
    lfinal = []
    dicc = pedidos(lista)
    for nombre in dicc:
        llarga.append((dicc[nombre], nombre))
    llarga.sort(reverse=True)
    for item in llarga[:3]:
        cant, nombre = item
        lfinal.append(nombre)
    return lfinal


def nombres(lista):
    ltot = []
    for item in lista:
        tipo, nombre, total = item
        if tipo == tipos(lista)[0]:
            ltot.append(nombre)

    return ltot


'''Prints funcion Nº1'''
# print(pedidos(lista))

'''Prints funcion Nº2'''
# print(tipos(lista))

'''Prints funcion Nº3'''
# print(nombres(lista))
