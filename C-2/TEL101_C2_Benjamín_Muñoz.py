# codigo por Raztorr


def minerales(roca):
    output = []
    for i in roca:
        if i not in output:
            output.append(i)
    return output


def pureza(roca):
    preout = len(minerales(roca)) / len(roca)
    output = float(round(preout, 2))
    return output


def pura(roca):
    if pureza(roca) == int(1):
        return True
    else:
        return False


def gemas(lista):
    output = []
    for i in lista:
        if pureza(i) == int(1):
            output.append(i)
    return output
