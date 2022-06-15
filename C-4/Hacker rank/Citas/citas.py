def afinidad(citas, Nombre1, Nombre2):
    persona1 = []
    persona2 = []
    cnt = 0
    for algo in citas[Nombre1]:
        if algo[1] == True:
            persona1.append(algo[0])
    for algo in citas[Nombre2]:
        if algo[1] == True:
            persona2.append(algo[0])
    for item in persona1:
        cnt += persona2.count(item)
    return cnt



print (afinidad({'nina': [('viajar', True), ('leer', False)], 'anna': [('nadar', False), ('pintura', True), ('dormir', True), ('mascotas', True)], 'paul': [('comer', True), ('mascotas', False)], 'carl': [('comer', True), ('dormir', True), ('bailar', False)], 'lore': [('leer', True), ('viajar', False)], 'john': [('pintura', True), ('mascotas', True), ('viajar', True), ('leer', False)]},  'nina', 'john' ))