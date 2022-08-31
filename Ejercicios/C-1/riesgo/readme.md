Entre las patologías más comunes en Chile se encuentran las enfermedades respiratorias. Dentro de los principales factores de riesgo están la presencia de más de 20 microgramos por metro cúbico () de material particulado en el aire, si es INVIERNO o PRIMAVERA, y si la persona es fumadora de cigarros.

Si una persona presenta a lo más uno de estos factores entonces tiene un 33% de probabilidad de contraer una enfermedad respiratoria. Si presenta 2, la probabilidad es de 66%. Si la persona presenta los 3 factores, entonces tiene un 90% de probabilidad de contraer una enfermedad respiratoria. La edad también influye en la probabilidad de enfermarse. La población de riesgo son los menores de 3 años y los mayores de 65, a quienes les aumenta en 10 puntos porcentuales la probabilidad de enfermarse, previamente calculada a partir de los factores de riesgo descritos.

Debe crear un programa para ser usado en un consultorio, que permita calcular el riesgo que tienen sus pacientes de sufrir enfermedades respiratorias. Para ello, solicite como entrada la edad de la persona que está siendo atendida, la cantidad de material particulado presente en el aire, el número del mes del año y si acaso la persona es fumadora. El programa debe mostrar por pantalla el porcentaje de riesgo de sufrir enfermedades respiratorias que tiene el paciente.

**Input Format**

-   Un número entero mayor que cero con la edad del paciente.
-   Un número entero mayor que cero con el material particulado presente en el aire.
-   Un número entero entre 1 y 12 con el mes del año.
-   Un texto con la palabra `SI` o `NO` para saber si la persona es fumadora.

**Constraints**

Para identificar la estación del año con el número de mes, asuma que `VERANO`:`1,2,3`, `OTOÑO`:`4,5,6`, `INVIERNO`:`7,8,9`, `PRIMAVERA`:`10,11,12`.

**Output Format**

Un número entero con el porcentaje de riesgo de sufrir enfermedades respiratorias que tiene el paciente.

##### Processing

-   [Testcase 0](chrome-extension://pcmpcfapbekmbjjkdalcgopdkipoggdi/#testcase1)
-   [Testcase 1](chrome-extension://pcmpcfapbekmbjjkdalcgopdkipoggdi/#testcase2)
-   [Testcase 2](chrome-extension://pcmpcfapbekmbjjkdalcgopdkipoggdi/#testcase3)

Your code did not pass this test case.

Input (stdin)

```
65
22
7
SI
```

Your Output (stdout)

##### ~ no response on stdout ~

Expected Output

```
90
```

Compiler Message

```
Wrong Answer
```

Your code did not pass this test case.

Input (stdin)

```
20
22
12
NO
```

Your Output (stdout)

##### ~ no response on stdout ~

Expected Output

```
66
```

Compiler Message

```
Wrong Answer
```

Your code did not pass this test case.

Input (stdin)

```
40
15
1
NO
```

Your Output (stdout)

##### ~ no response on stdout ~

Expected Output

```
33
```

Compiler Message

```
Wrong Answer
```
