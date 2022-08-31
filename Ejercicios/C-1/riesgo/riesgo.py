edad = (int(input('Edad')))
particulas = (int(input('Particulas')))
mes = (int(input('Mes')))
fuma = (str(input('Fuma')))
estacionaf = range(7, 13)
probabilidad = 0
edadprob = 0
final = 0

if mes in estacionaf:
    probabilidad = probabilidad + 1
if fuma == 'SI':
    probabilidad = probabilidad + 1

if particulas > 20:
    probabilidad = probabilidad + 1

if probabilidad in range(0, 2):
    final = 33
elif probabilidad == 2:
    final = 66
elif probabilidad == 3:
    final = 90

if edad < 3:
    final = final + 10
    print(final)
elif edad > 65:
    final = final + 10
    print(final)
else:
    print(final)
