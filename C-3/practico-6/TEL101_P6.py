def rankear(nombre_archivo, rank_min, rank_max):
    biblio = open(nombre_archivo, 'r', encoding="UTF-8")
    lista=[]
    for linea in biblio:
        titulo, tipo, rating, ranking, episodios, genero, fecha = linea.strip().split('|')
        if float(ranking) >= rank_min and float(ranking) <= rank_max:
            nuevo = open(f'{titulo}.txt', 'w', encoding="UTF-8")
            a = genero.strip().split(',')
            dia, mes, año = fecha.strip().split('-')
            nuevo.write(f'#{ranking} {titulo} ({rating})\n\nEstreno: {tipo}, {año}\nEpisodios: {episodios}\nGéneros:\n')
            nuevo.close()
            for cat in a:
                appendcat = open(f'{titulo}.txt', 'a', encoding="UTF-8")
                appendcat.write(f'\t{cat} \n')
                appendcat.close()
            lista.append(float(rating))
    promedio = round((sum(lista) / len(lista)), 2)
    biblio.close()
    return promedio

print(rankear("animes.txt", 4, 6))