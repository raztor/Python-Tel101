##Codigo por Raztor
#########################CODIGO SIN TERMINAR####################
cantmensajes=int(input('Ingrese la cantidad de mensajes:' ))
nintento=0
palabras= []
fnlist=[]
vocales='aeiouAEIOU'
while nintento<cantmensajes:
    cant = 0
    vintento = 0
    palabras.append(str(input('Ingrese mensaje: ')))
    nintento=nintento+1

    for voc in ''.join(palabras):
        if voc in vocales:
            cant += 1
    while cant>vintento:
        for antvoc in vocales:
            # replacing vowel with the specified character
            palabras=palabras.replace(antvoc, antvoc+'py')
            vintento=vintento+1
            print(palabras)

