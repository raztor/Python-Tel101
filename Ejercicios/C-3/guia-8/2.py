frase = str(input('Ingrese una frase: '))
frase = frase.split()
frasefin = ('')
vocales = ('aeiou')

for palabra in frase:
    if palabra[-1].lower() in vocales:
        frasefin += (palabra[:-1] + 'e ')
    else:
        frasefin += (palabra + ' ')

print(frasefin)