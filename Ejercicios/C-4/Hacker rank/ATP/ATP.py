# Completar esto solamente
def ranking(lista, annio):
    jugadores = {}
    listafin = []
    lfin = []
    contador = 0
    for item in lista:
        torneo, year, nombre, puntaje = item
        if year == annio:
            try:
                oldval = jugadores[nombre]
                jugadores[nombre] = puntaje+oldval
            except:
                jugadores[nombre] = puntaje
    list = [(name, value) for name, value in jugadores.items()]
    for item in list:
        nombre, value = item
        listafin.append((value,nombre))
    listafin.sort(reverse=True)

    for item in listafin:
        contador += 1
        value, nombre = item
        posc = contador
        lfin.append((posc, nombre, value))

    return lfin


# Esto se usa para ejecutar y cambiar los datos
print(ranking([('Australian Open', 2004, 'Roger Federer', 2000), ('Qatar Exxon Mobil Open', 2017, 'Novak Djokovic', 250), ("Internazionali BNL d'Italia", 1998, 'Marcelo Rios', 1000), ('Australian Open', 2017, 'Roger Federer', 2000), ('Wimbledon', 2017, 'Roger Federer', 2000), ('Rogers Cup', 2017, 'Alex Zverev', 1000), ('US Open', 2017, 'Rafael Nadal', 2000), ('Wimbledon', 1998, 'Pete Sampras', 2000), ('Roland Garros', 2017, 'Rafael Nadal', 2000), ('Rio Open', 2017, 'Dominic Thiem', 500), ('Barcelona', 2017, 'Rafael Nadal', 500)], 2017))
#print(ranking(eval(input()), int(input())))