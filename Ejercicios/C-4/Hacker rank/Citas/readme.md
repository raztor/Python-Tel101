Una página web de citas amorosas utiliza un diccionario para almacenar información de personas que buscan pareja. Las llaves del diccionario son los nombres de las personas y el valor es una lista de tuplas con todas las cosas que a la persona le gustan y disgustan. A continuación, un ejemplo:

```
{
'nina': [('viajar',True),('leer',False)],
'anna': [('nadar',False),('pintura',True),('dormir',True),('mascotas',True)],
'paul': [('comer',True),('mascotas',False)],
'carl': [('comer',True),('dormir',True),('bailar',False)],
'lore': [('leer',True),('viajar',False)],
'john': [('pintura',True),('mascotas',True),('viajar',True),('leer',False)],
... }

```

Cada tupla contiene dos elementos, una cosa y un booleano. Si el booleano es `True` es porque esa cosa le gusta a la persona. Por el contrario, si el booleano es `False` es porque esa cosa no le gusta a la persona.

Diseñe la función `afinidad(citas, Nombre1, Nombre2)` que recibe un diccionario como el anterior llamado `citas` y el nombre de dos personas (`Nombre1` y `Nombre2`). Esta función debe retornar la cantidad de cosas que le gustan a ambas personas.

**Input Format**

Un diccionario con el formato del ejemplo y dos textos con el nombre de dos personas que están dentro del diccionario.

**Constraints**

-   Los nombres de ambas personas estarán siempre en el diccionario.
-   Asuma que los datos siempre serán correctos, es decir, respetarán la estructura mostrada en el ejemplo. Sin embargo, la cantidad de elementos y valores mostrados en el ejemplo pueden cambiar.

**Output Format**

Un número entero indicando la cantidad de cosas que ambas personas gustan.

**Sample Input 0**

```
{'nina': [('viajar', True), ('leer', False)], 'anna': [('nadar', False), ('pintura', True), ('dormir', True), ('mascotas', True)], 'paul': [('comer', True), ('mascotas', False)], 'carl': [('comer', True), ('dormir', True), ('bailar', False)], 'lore': [('leer', True), ('viajar', False)], 'john': [('pintura', True), ('mascotas', True), ('viajar', True), ('leer', False)]}
nina
john

```

**Sample Input 1**

```
{'nina': [('viajar', True), ('leer', False)], 'anna': [('nadar', False), ('pintura', True), ('dormir', True), ('mascotas', True)], 'paul': [('comer', True), ('mascotas', False)], 'carl': [('comer', True), ('dormir', True), ('bailar', False)], 'lore': [('leer', True), ('viajar', False)], 'john': [('pintura', True), ('mascotas', True), ('viajar', True), ('leer', False)]}
nina
lore

```

**Sample Input 2**

```
{'nina': [('viajar', True), ('leer', False)], 'anna': [('nadar', False), ('pintura', True), ('dormir', True), ('mascotas', True)], 'paul': [('comer', True), ('mascotas', False)], 'carl': [('comer', True), ('dormir', True), ('bailar', False)], 'lore': [('leer', True), ('viajar', False)], 'john': [('pintura', True), ('mascotas', True), ('viajar', True), ('leer', False)]}
john
lore

```