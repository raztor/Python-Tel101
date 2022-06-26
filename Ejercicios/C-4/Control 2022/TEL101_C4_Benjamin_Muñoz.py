lista = [
('2021-2', 'Denis', 'TEL101', 60),
('2021-1', 'Nora', 'TEL101', 88),
('2020-2', 'Nora', 'ELO320', 59),
('2021-2', 'Nora', 'DEW100', 54),
('2021-2', 'Yuriko', 'TEL101', 68),
('2021-2', 'Nora', 'TEL101', 9),
('2021-2', 'Mike', 'TEL101', 55),
('2021-2', 'Yuriko', 'IWG101', 100),
('2021-2', 'Denis', 'FIS100', 55),
('2021-2', 'Mike', 'FIS100', 71)]


def f1(semestre, lista):
    dicc = {}
    for linea in lista:
        sem, estudiante, asignatura, promedio = linea
        if semestre == sem:
            if promedio >= 55:
                if asignatura in dicc:
                    dicc[asignatura].append(promedio)
                else:
                    dicc[asignatura] = [promedio]
            elif promedio < 55 and asignatura not in dicc:
                dicc[asignatura] = []
    return dicc


'''El filtro de notas aprobadas lo realice al usar la funcion numero 1'''


def f2(semestre, lista):
    promedios = f1(semestre, lista)
    flista = []
    for item in promedios:
        if promedios[item]:
            maxim = max(promedios[item])
            minim = min(promedios[item])
            prom = round((sum(promedios[item])/len(promedios[item])))
            flista.append((item, maxim, minim, prom))

    return flista


'''Prints funcion 1'''
# print(f1("2021-2", lista))

'''Prints funcion 2'''
# print(f2("2021-2", lista))
