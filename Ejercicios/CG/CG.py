from matplotlib import pyplot as pt
def costo(largo, ancho):
    if largo > 50 or ancho > 300:
        valor = 2*largo + 3*ancho
    else:
        valor = largo + 2*ancho
    return valor

def grafico(nombre_archivo, lugar):
    # Persona; Destino; Medidas
    archivo = open(nombre_archivo, "r")
    cantidad = {}
    total_costo = []
    total_ciudades = []
    total_env_ciudades = []
    for linea in archivo:
        persona, destino, medidas = linea.strip().split(";")
        if destino in cantidad:
            cantidad[destino] += 1
        else:
            cantidad[destino] = 1
        if lugar == destino:
            largo, ancho = medidas.split(",")
            largo = int(largo)
            ancho = int(ancho)
            total_costo.append(costo(largo, ancho))

    pt.bar(total_ciudades, total_env_ciudades)
    pt.show()




print(grafico('encomiendas.txt', 'Santiago'))