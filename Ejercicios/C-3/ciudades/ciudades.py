def separar(nombre_archivo, pais):
    archivo = open(nombre_archivo, 'r', encoding='UTF8')
    archnuevo = open(f'{pais}.txt', 'w', encoding='UTF8')
    for linea in archivo:
        pact, ciudades = linea.strip().split(':')
        if pais == pact:
            pfinal = pact
            cfinal = ciudades
    archnuevo.write(f'Ciudades de {pfinal}:\n')
    archivo.close()
    archnuevo.close()
    cfinal = cfinal.split(',')
    archnuevo = open(f'{pais}.txt', 'a', encoding='UTF8')
    for city in cfinal:
        archnuevo.write(f'\t{city}\n')
    return len(cfinal)

print(separar('ciudades.txt', 'Chile'))