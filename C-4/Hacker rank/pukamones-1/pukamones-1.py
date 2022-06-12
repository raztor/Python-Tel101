# Completar esto solamente
def buscar(pukamones, numero):
    for pukamon in pukamones:
        nombre, npuk, categoria = pukamon
        if npuk == numero:
            return nombre
    return '???'


# Esto se usa para ejecutar y cambiar los datos
print (buscar( eval(input() ), int(input()) ))