input1=str(input())
numeros=('1234567890')
intento=0
pfinal=''
valor=0
for in1 in input1:
    if in1 in numeros:
        valor=int(in1)
    else:
        in1=in1*valor
        pfinal=pfinal+in1
print(pfinal)