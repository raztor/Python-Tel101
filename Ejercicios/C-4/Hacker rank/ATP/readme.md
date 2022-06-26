La Asociación de Tenistas Profesionales (ATP) utiliza una lista de tuplas para llevar registro de los torneos disputados cada año. La lista almacena en tuplas el nombre del torneo, el año que se disputó, el nombre de un jugador que participó y los puntos que obtuvo. Un ejemplo se muestra a continuación:

```
[('Australian Open', 2004, 'Roger Federer', 2000),
('Qatar Exxon Mobil Open', 2017, 'Novak Djokovic', 250),
("Internazionali BNL d'Italia", 1998, 'Marcelo Rios', 1000),
('Australian Open', 2017, 'Roger Federer', 2000),
... ]

```

Considere que cada torneo puede aparecer muchas veces en la lista porque distintos jugadores participaron y en diferentes años. Los puntos también son variables porque depende de la cantidad de partidos ganados por el jugador y del tipo de torneo.

Desarrolle la función `ranking(lista, annio)` que recibe una lista de tuplas como la mostrada en el ejemplo y el entero `annio` que representa algún año. La función debe retornar una lista de tuplas, donde cada tupla tenga 3 elementos:

-   Número entero incremental que designa la posición en el ranking ATP.
-   Nombre del jugador en esa posición del ranking.
-   Puntos acumulados durante el año por parte de ese jugador.

La lista debe estar ordenada de forma ascendente según la posición en el ranking ATP de cada jugador. El ranking se calcula de acuerdo a la suma de los puntos obtenidos durante el año por cada jugador.

**Input Format**

Una lista de tuplas con el formato del ejemplo y un entero con el año.

**Constraints**

Asuma que los datos siempre serán correctos, es decir, respetarán la estructura mostrada en el ejemplo. Sin embargo, la cantidad de elementos y valores mostrados en el ejemplo pueden cambiar.

**Output Format**

Una lista de tuplas, donde cada tupla tiene el formato `(posición,nombre,puntos)`, ordenada de mayor a menor `puntos`.

**Sample Input 0**

```
[('Australian Open', 2004, 'Roger Federer', 2000), ('Qatar Exxon Mobil Open', 2017, 'Novak Djokovic', 250), ("Internazionali BNL d'Italia", 1998, 'Marcelo Rios', 1000), ('Australian Open', 2017, 'Roger Federer', 2000), ('Wimbledon', 2017, 'Roger Federer', 2000), ('Rogers Cup', 2017, 'Alex Zverev', 1000), ('US Open', 2017, 'Rafael Nadal', 2000), ('Wimbledon', 1998, 'Pete Sampras', 2000), ('Roland Garros', 2017, 'Rafael Nadal', 2000), ('Rio Open', 2017, 'Dominic Thiem', 500), ('Barcelona', 2017, 'Rafael Nadal', 500)]
2017

```

**Sample Output 0**

```
[(1, 'Rafael Nadal', 4500), (2, 'Roger Federer', 4000), (3, 'Alex Zverev', 1000), (4, 'Dominic Thiem', 500), (5, 'Novak Djokovic', 250)]

```