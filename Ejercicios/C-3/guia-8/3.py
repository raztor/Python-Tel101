def verificar_numero(numero, carton):
    carton = carton.split('-')
    carton = [float(i) for i in carton]
    if numero in carton:
        return True
    else:
        return False

print(verificar_numero(2,'1-12-54-5'))