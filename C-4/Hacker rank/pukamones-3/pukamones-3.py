# Completar esto solamente
def pukadex(pukamones, tipo):
    lista = []
    nlista = []

    for pukamon in pukamones:
        nombre, num, cat = pukamon
        if tipo in cat:
            lista.append((int(num), nombre))

    lista.sort()

    for item in lista:
        num, nombre = item
        nlista.append(nombre)

    return nlista


# Esto se usa para ejecutar y cambiar los datos
print(pukadex(eval(input()), input()))