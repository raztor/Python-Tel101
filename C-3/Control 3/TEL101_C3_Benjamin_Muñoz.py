def cancionero(nombre_archivo, artista):
    txt = open(nombre_archivo, 'r', encoding='UTF8')
    newtxt = open(f'{artista}.txt', 'w', encoding='UTF8')
    newtxt.write(f'Canciones de {artista}:\n')
    newtxt.close()
    total = 0
    promedio = []
    newtxt = open(f'{artista}.txt', 'a', encoding='UTF8')
    for linea in txt:
        cantante, cancion, año, popularidad, generos = linea.split('|')
        if cantante == artista:
            if int(popularidad) >= 0 and int(popularidad) <= 33:
                nivel = 'baja'
            elif int(popularidad) >= 34 and int(popularidad) <= 66:
                nivel = 'media'
            elif int(popularidad) >= 67 and int(popularidad) <= 100:
                nivel = 'alta'
            newtxt.write(f'\t{cancion} ({año}) tiene popularidad {nivel} ({popularidad}).\n')
            total += 1
            promedio.append(int(popularidad))
    promedio = int(round(sum(promedio)/len(promedio), 0))
    newtxt.write(f'{artista} tiene promedio {promedio} entre sus {total} canciones.')

    if int(promedio) >= 0 and int(promedio) <= 33:
        x = 'baja'
    elif int(promedio) >= 34 and int(promedio) <= 66:
        x = 'media'
    elif int(promedio) >= 67 and int(promedio) <= 100:
        x = 'alta'
    newtxt.close()
    txt.close()
    return x

#print(cancionero("canciones.txt", "Britney Spears"))
#print(cancionero("canciones.txt", "Red Hot Chili Peppers"))