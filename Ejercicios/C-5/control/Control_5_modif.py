from matplotlib import pyplot as pp


def tendencia(nombre_archivo, *input_regiones):
    archivo = open(nombre_archivo, 'r', encoding='UTF8')
    mStyles = [".", "o", "v", "^", "<", ">", "8", "s", "p", "P", "*", "h", "H", "+", "x", "X",
               "D", "d", "|", "_"]
    regiones = {}
    lista = []
    for linea in archivo:
        casos_final = []
        region, casos = linea.strip().split(':')
        casos = casos.split(',')
        for caso in casos:
            casos_final.append(int(caso))
        if region in input_regiones:
            regiones[region] = casos_final
    archivo.close()
    contar = 0
    for n in regiones:
        contar += 1
        cont = -1
        x = []
        lista.append((sum(regiones[n]), n))
        for dia in regiones[n]:
            cont += 1
            x.append(cont)
        pp.plot(x, regiones[n], label=n, marker=mStyles[contar])

    pp.grid(color='gray', linestyle='--', linewidth=0.2)
    pp.ylabel('Casos')
    pp.xlabel('Días')
    pp.legend()
    pp.show()

    tupl_max = max(lista)
    return tupl_max[1]

print(tendencia("casos.txt", "Tarapaca", "Valparaiso", 'Coquimbo', "Biobio"))
