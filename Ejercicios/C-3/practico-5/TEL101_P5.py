def libros(nombre_archivo, autor):
    biblio = open(nombre_archivo, 'r', encoding="UTF-8")
    nuevo = open(f'{autor}.txt', 'w', encoding="UTF-8")
    print(f'Libros de {autor}:')
    contador = 0
    listprom = []
    notmay=0
    libronotmay=''
    añomay = 0
    for linea in biblio:
        if autor in linea:
            contador += 1
            libro, año, Autor, nota = linea.strip().split('|')
            if float(nota)>notmay:
                libronotmay = libro
                notmay = float(nota)
                añomay = int(año)
            listprom.append(float(nota))
            nuevo.write(f'\t {contador}. {libro} del año {año}.\n')
    promedio = round(sum(listprom)/len(listprom), 2)
    nuevo.write(f'El promedio de notas de {autor} es {promedio}.\nEl libro con mejor nota es {libronotmay} {añomay} con nota {notmay}')
    return (contador)

print(libros("libros.txt", "Ray Bradbury"))
