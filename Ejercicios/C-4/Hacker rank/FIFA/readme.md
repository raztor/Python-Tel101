En un diccionario se almacenan los resultados de cada partido en un grupo del Mundial de Fútbol. Las llaves son tuplas de dos elementos con los paises que se enfrentaron y los valores son tuplas con los goles que cada equipo anotó. A continuación, puede encontrar un ejemplo:

```
{('Australia','Brasil'):(3,2),
('Chile','Suecia'):(0,2),
('EE.UU.','Tailandia'):(13,0),
('Suecia','Tailandia'):(5,1),
('EE.UU.','Chile'):(3,0), ... }

```

`Australia` le ganó a `Brasil` 3 goles a 2, `Chile` perdió con `Suecia` 0 goles a 2, etc.

Escriba la función `tabla(resultados)`, que recibe un diccionario con el formato anterior y retorna una lista de tuplas con todos los paises ordenados por puntos. Si hay empate en puntos, la diferencia de gol es el segundo criterio de ordenamiento.

Se otorgan 3 puntos por partido ganado, 1 por partido empatado y 0 por partido perdido.

**Input Format**

Un diccionario con el formato del ejemplo.

**Constraints**

Asuma que los datos siempre serán correctos, es decir, respetarán la estructura mostrada en el ejemplo. Sin embargo, la cantidad de elementos y valores mostrados en el ejemplo pueden cambiar.

**Output Format**

Una lista de tuplas en formato: `[(pais,puntos,difgol), (pais,puntos,difgol), (pais,puntos,difgol), ...]`, ordenada por puntos y luego diferencia de gol.

**Sample Input 0**

```
{('Australia', 'Brasil'): (3, 2), ('Chile', 'Suecia'): (0, 2), ('EE.UU.', 'Tailandia'): (13, 0), ('Suecia', 'Tailandia'): (5, 1), ('EE.UU.', 'Chile'): (3, 0)}

```

**Sample Output 0**

```
[('EE.UU.', 6, 16), ('Suecia', 6, 6), ('Australia', 3, 1), ('Brasil', 0, -1), ('Chile', 0, -5), ('Tailandia', 0, -17)]

```

**Sample Input 1**

```
{('Brasil', 'Venezuela'): (3, 0), ('Colombia', 'Ecuador'): (1, 0), ('Argentina', 'Chile'): (1, 1), ('Paraguay', 'Bolivia'): (3, 1), ('Colombia', 'Venezuela'): (0, 0), ('Brasil', 'Peru'): (4, 0)}

```

**Sample Output 1**

```
[('Brasil', 6, 7), ('Colombia', 4, 1), ('Paraguay', 3, 2), ('Chile', 1, 0), ('Argentina', 1, 0), ('Venezuela', 1, -3), ('Ecuador', 0, -1), ('Bolivia', 0, -2), ('Peru', 0, -4)]

```