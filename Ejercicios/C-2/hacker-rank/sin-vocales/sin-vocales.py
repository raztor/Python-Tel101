wrd = input()
rmvoc = ''
for letras in wrd:
    if letras not in "aeiou":
        rmvoc += letras
print(rmvoc)