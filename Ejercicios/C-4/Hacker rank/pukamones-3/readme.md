Los Pukamones son criaturas mágicas con características animales que pueden ser capturados con una Pukabola para ser entrenados.

![image](https://s3.amazonaws.com/hr-assets/0/1624226595-870ee2d17b-pukamones.png)

El Profesor Poak ha estudiado a los Pukamones durante siglos y creó una lista de tuplas para almacenar a todos los Pukamones conocidos. Cada tupla tiene tres elementos, el Nombre en formato texto, el Número en formato entero y una lista con los Tipos del Pukamon de largo variable. Un ejemplo se muestra a continuación:

```
[('Pukachu',25,['electrico']),
('Vinosur',3,['planta','veneno']),
('Chorizord',6,['fuego','volador']),
('Chukorito',152,['planta']),
('Matepod',11,['bicho']),
('Bulmasaur',1,['planta','veneno']),
('Blistoise',9,['agua']),
('Coterpi',10,['bicho']),
('Escuartupla',7,['agua']),
('Hakuna',14,['bicho','veneno']),
('NewTwo',150,['psiquico']),
('Kaku Topo',785,['electrico','hada']),
('Lucagrio',448,['lucha','acero'])]

```

**TAREA 3.** Escriba la función `pukadex(pukamones, tipo)` que recibe una lista de tuplas con los Pukamones y un texto con un Tipo de Pukamon. Esta función debe retornar una lista con los Nombres de todos los Pukamones de ese Tipo ordenados por Número.

**Input Format**

Una lista de tuplas con el formato del ejemplo y un texto con el Tipo de un Pukamon.

**Constraints**

Asuma que los datos siempre serán correctos, es decir, respetarán la estructura mostrada en el ejemplo. Sin embargo, la cantidad de elementos y valores mostrados en el ejemplo pueden cambiar.

**Output Format**

Una lista con los Nombres de los Pukamones del tipo recibido como parámetro. Cada Pukamon debe aparecer en orden de acuerdo a su Número.

**Sample Input 0**

```
[('Pukachu', 25, ['electrico']), ('Vinosur', 3, ['planta', 'veneno']), ('Chorizord', 6, ['fuego', 'volador']), ('Chukorito', 152, ['planta']), ('Matepod', 11, ['bicho']), ('Bulmasaur', 1, ['planta', 'veneno']), ('Blistoise', 9, ['agua']), ('Coterpi', 10, ['bicho']), ('Escuartupla', 7, ['agua']), ('Hakuna', 14, ['bicho', 'veneno']), ('NewTwo', 150, ['psiquico']), ('Kaku Topo', 785, ['electrico', 'hada']), ('Lucagrio', 448, ['lucha', 'acero'])]
planta

```

**Sample Output 0**

```
['Bulmasaur', 'Vinosur', 'Chukorito']

```

**Sample Input 1**

```
[('Pukachu', 25, ['electrico']), ('Vinosur', 3, ['planta', 'veneno']), ('Chorizord', 6, ['fuego', 'volador']), ('Chukorito', 152, ['planta']), ('Matepod', 11, ['bicho']), ('Bulmasaur', 1, ['planta', 'veneno']), ('Blistoise', 9, ['agua']), ('Coterpi', 10, ['bicho']), ('Escuartupla', 7, ['agua']), ('Hakuna', 14, ['bicho', 'veneno']), ('NewTwo', 150, ['psiquico']), ('Kaku Topo', 785, ['electrico', 'hada']), ('Lucagrio', 448, ['lucha', 'acero'])]
agua

```

**Sample Output 1**

```
['Escuartupla', 'Blistoise']

```