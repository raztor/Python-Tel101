# Completar esto solamente
def filtrar(pukamones, tipo):
    lista = []
    for pukamon in pukamones:
        nombre, num, categoria = pukamon
        if tipo in categoria:
            newpk = (num, nombre)
            lista.append(newpk)
    return lista


# Esto se usa para ejecutar y cambiar los datos
print (filtrar( eval(input() ), input() ))