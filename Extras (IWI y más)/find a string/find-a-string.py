def count_substring(string, sub_string):
    cant = 0
    minim = 0
    cont = 0
    maxim = len(sub_string)
    sub_string = list(sub_string)
    while cont < len(string):
        string = list(string)
        sect = string[minim:maxim]
        if sub_string == sect:
            cant += 1
        minim += 1
        maxim += 1
        cont += 1
    return cant
print(count_substring('ABCDCDC', 'CDC'))