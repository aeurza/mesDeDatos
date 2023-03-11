ntroducción
Completado
100 XP
1 minuto
Las matemáticas formarán parte de casi todos los proyectos que cree en todo su recorrido como desarrollador. Si es científico de datos, es posible que esté haciendo cálculos bastante complejos. Si va a crear sitios web, puede que determine los precios o los artículos de un carro de compra. Al igual que cualquier otro lenguaje de programación, Python proporciona numerosos operadores y bibliotecas para hacer operaciones matemáticas.

Escenario: Creación de un programa para calcular la distancia entre planetas
Imagine que crea un programa para calcular la distancia entre planetas. El programa permite que un usuario escriba las distancias de dos planetas respecto al sol y calcula la distancia entre esos dos planetas. Además, quiere proporcionar la distancia tanto en millas como en kilómetros.

¿Qué aprenderá?
En este módulo, explorará las principales funcionalidades matemáticas de Python. Aprenderá lo siguiente:

Los operadores matemáticos disponibles en Python.
El orden de las operaciones.
Cómo convertir cadenas en números.
¿Cuál es el objetivo principal?
Basarse en la potencia de los operadores matemáticos al crear un programa de Python.

tipos de variables...
int = enteros
float = numeros con deceimales
abs =  valor absoluto
round = redondeo


# Biblioteca matemática

Python tiene bibliotecas para proporcionar operaciones y cálculos más avanzados. Una de las más comunes es la biblioteca math. math permite hacer el redondeo con floor y ceil, proporcionar el valor de pi y muchas otras operaciones. Veamos cómo usar esta biblioteca para redondear hacia arriba o hacia abajo.

El redondeo de números permite quitar la parte decimal de un número de punto flotante. Puede optar por redondear siempre hacia arriba al número entero más cercano si usa ceil, o hacia abajo si usa floor.


from math import ceil, floor

round_up = ceil(12.5)
print(round_up)

round_down = floor(12.5)
print(round_down)



