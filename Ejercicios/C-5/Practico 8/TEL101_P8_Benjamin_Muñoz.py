from matplotlib import pyplot as pp


def migraciones(nombre_archivo, ano):
    archivo = open(nombre_archivo, 'r', encoding='UTF8')
    total = {}
    for linea in archivo:
        persona, pais, year = linea.strip().split(';')
        year = int(year)
        if year == ano:
            if pais in total:
                total[pais] += 1
            else:
                total[pais] = 1
    x = list(total.keys())
    y = list(total.values())
    pp.bar(x, y, label='pais')
    pp.ylabel('Inmigrantes')
    pp.title(f'Migraciones en el año {ano}')
    pp.savefig(f'{ano}.pdf')
    pp.show()

    return sum(y)


print(migraciones("personas.txt", 2017))
