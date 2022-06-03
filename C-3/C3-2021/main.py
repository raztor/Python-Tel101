def promedio(archivo, genero):
    pel = open(archivo, 'r', encoding='UTF8')
    prom = []
    for linea in pel:
        titulo, año, generos, directores, actores, calif = linea.split('|')
        if genero in generos:
            prom.append(float(calif))
    try:
        prfin = round(sum(prom)/len(prom), 2)
        return prfin
    except ZeroDivisionError:
        return 0.0
    pel.close()

def actores(archivo, genero):
    actarch = open(archivo, 'r', encoding='UTF8')
    cant = 0
    for linea in actarch:
        titulo, año, generos, directores, actores, calif = linea.split('|')
        actores = actores.split(',')
        if genero in generos:
            if float(calif) > promedio(archivo, genero):
                nuevotxt = open(f'{titulo}.txt', 'w', encoding='UTF8')
                nuevotxt.write(f'{titulo} {año}\n\nDirigida por {directores}\n\n')
                nuevotxt.close()
                nuevotxt = open(f'{titulo}.txt', 'a', encoding='UTF8')
                for actor in actores:
                    nuevotxt.write(f'{actor}\n')
                cant += 1
    return cant
print(actores("Top10.txt", "Crime"))