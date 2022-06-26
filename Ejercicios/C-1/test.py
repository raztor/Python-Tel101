vida=0
hambre=0
dias=int(input("Ingrese dias de vida:"))
x = 0
mas=0
total=0
diamas= 0
while vida<dias:
    x += 1
    print("Dia",x)
    hambre=int(input("Ingrese nivel de hambre:"))
    hambrent=0
    alimento=0
    alidia= 0
    while hambrent<hambre:
      ali = str(input("Ingrese un alimento:"))
      if ali == "salchipapa":
        hambrent +=1
        alimento +=1
        total +=1
        alidia += 1
      if ali == "sumaruchan":
        hambrent +=2
        alimento +=1
        total +=1
        alidia +=1
      if ali == "supapajohn":
        hambrent +=3
        alimento +=1
        total +=1
        alidia +=1
      if ali != "supapajohn" and ali !="sumaruchan" and ali != "salchipapa":
        hambrent += 0
        alimento +=1
        alidia += 1
        total += 1
    if mas<alimento:
      mas=alimento
      diamas = x
    elif mas>alimento:
      mas= mas
      diamas = diamas
    print("En el dia",x,"se consumieron",alidia,"alimentos")
    vida +=1
if vida == dias:
  print("se consumieron en total", total,"alimentos")
  print("El dia", diamas," fue el mas gloton con", mas)