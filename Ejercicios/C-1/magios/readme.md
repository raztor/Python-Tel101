Los Magios es una organización secreta que controla el mundo desde las sombras. Ellos organizan reuniones para discutir el destino de la humanidad, pero son muy estrictos sobre quienes pueden ser parte de la comunidad. Escriba un programa que reciba como entrada un número entero que representa la cantidad de integrantes de la reunión (aforo permitido). Luego, un texto que representa el nombre de las personas que tienen prohibido el acceso y finalmente recibirá los nombres de las personas que ingresan a la reunión hasta que se cumpla el aforo permitido. Cuando ingrese una persona con acceso garantizado se imprimirá la palabra `Bienvenid@`, seguida del nombre de la persona, seguida del contador de personas ingresadas con respecto al total, separando por un espacio cada palabra. Si se recibe el nombre de una persona con acceso denegado se imprimirá la frase `No se admiten`, seguida del nombre de la persona.

**Input Format**

-   Un número entero con el aforo permitido a la reunión.
-   Un texto con el nombre prohibido.
-   Varios textos con nombres de personas que desean ingresar a la reunión.

**Constraints**

Asuma que los datos corresponden a su tipo, pero la cantidad de nombres depende del aforo permitido. Cuando se reciba un nombre con acceso denegado no cuenta como integrante de la reunión.

**Output Format**

Para cada `NOMBRE` que desea ingresar a la reunión, hay dos posibles mensajes de salida:

`Bienvenid@ NOMBRE N / AFORO`, o bien `No se admiten NOMBRE`,

donde `N` es la cantidad de personas con acceso permitido actualmente en la reunión y `AFORO` representa el máximo permitido.

**Sample Input 0**

```
5
Homero
Juan
Pedro
Homero
Ana
Homero Archundia
Homero
Diego

```

**Sample Output 0**

```
Bienvenid@ Juan 1 / 5
Bienvenid@ Pedro 2 / 5
No se admiten Homero
Bienvenid@ Ana 3 / 5
Bienvenid@ Homero Archundia 4 / 5
No se admiten Homero
Bienvenid@ Diego 5 / 5

```

**Sample Input 1**

```
3
juan
don juan
juan
juanito
juan
Juan

```

**Sample Output 1**

```
Bienvenid@ don juan 1 / 3
No se admiten juan
Bienvenid@ juanito 2 / 3
No se admiten juan
Bienvenid@ Juan 3 / 3

```

##### Processing

-   [Testcase 0](chrome-extension://pcmpcfapbekmbjjkdalcgopdkipoggdi/#testcase1)
-   [Testcase 1](chrome-extension://pcmpcfapbekmbjjkdalcgopdkipoggdi/#testcase2)

Your code did not pass this test case.

Input (stdin)

```
5
Homero
Juan
Pedro
Homero
Ana
Homero Archundia
Homero
Diego
```

Your Output (stdout)

##### ~ no response on stdout ~

Expected Output

```
Bienvenid@ Juan 1 / 5
Bienvenid@ Pedro 2 / 5
No se admiten Homero
Bienvenid@ Ana 3 / 5
Bienvenid@ Homero Archundia 4 / 5
No se admiten Homero
Bienvenid@ Diego 5 / 5
```

Compiler Message

```
Wrong Answer
```

Your code did not pass this test case.

Input (stdin)

```
3
juan
don juan
juan
juanito
juan
Juan
```

Your Output (stdout)

##### ~ no response on stdout ~

Expected Output

```
Bienvenid@ don juan 1 / 3
No se admiten juan
Bienvenid@ juanito 2 / 3
No se admiten juan
Bienvenid@ Juan 3 / 3
```

Compiler Message

```
Wrong Answer
```
