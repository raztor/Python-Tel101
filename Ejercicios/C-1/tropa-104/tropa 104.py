import os
km=(int(input('KM')))
tita=(int(input('Titanes')))
integrantes=(int(input('Integrantes')))
consumidopp=((3*km)+(2*tita))
consumidotot=(consumidopp*integrantes)
print (str(consumidopp) + ' Litros', str(consumidotot) + ' Litros', sep=os.linesep)
