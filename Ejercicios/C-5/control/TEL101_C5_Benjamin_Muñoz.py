from matplotlib import pyplot as pp


def tendencia(nombre_archivo, region1, region2):
    archivo = open(nombre_archivo, 'r', encoding='UTF8')
    regiones = {}
    lista = []
    for linea in archivo:
        casos_final = []
        region, casos = linea.strip().split(':')
        casos = casos.split(',')
        for caso in casos:
            casos_final.append(int(caso))
        if region == region1 or region == region2:
            regiones[region] = casos_final
    archivo.close()
    for n in regiones:
        cont = -1
        x = []
        lista.append((sum(regiones[n]), n))
        for dia in regiones[n]:
            cont += 1
            x.append(cont)
        if n == region1:
            pp.plot(x, regiones[n], label=n, marker='o')
        elif n == region2:
            pp.plot(x, regiones[n], label=n, marker='s')

    pp.grid(color='gray', linestyle='--', linewidth=0.2)
    pp.ylabel('Casos')
    pp.xlabel('Días')
    pp.legend()
    pp.show()

    tupl_max = max(lista)
    return tupl_max[1]

print(tendencia("casos.txt", "Tarapaca", "Valparaiso"))
