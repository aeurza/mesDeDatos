# Introducción
# Completado

# Como desarrollador, trabajará con frecuencia con conjuntos de datos. Es posible que tenga que administrar varios nombres, edades o direcciones. Almacenar cada valor en una variable individual hace que el código sea más difícil de leer y escribir. Para almacenar varios valores, puede usar una lista de Python.

# Escenario: Trabajar en una aplicación de planetario
# Imagine es un desarrollador que quiere crear una aplicación para trabajar con una lista de planetas. Quiere preguntar al usuario el nombre de un planeta y mostrar los planetas más cercanos al sol y los más alejados de él.

# En este módulo, descubrirá cómo usar listas de Python y algunas de las operaciones más comunes.

# ¿Qué descubriré?
# Después de completar este módulo, podrá:

# Identificar cuándo se debe usar una lista.
# Crea una lista.
# Acceder a un elemento determinado de una lista mediante índices.
# Insertar elementos al final de una lista.
# Ordenar y segmentar una lista.
# ¿Cuál es el objetivo principal?
# Al final de este módulo, comprenderá cuándo usar una estructura de lista y cómo puede ayudar a organizar los datos.


# LAS LISTAS SE DEFINEN POR:
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

# para recorrer la lista y siempre empieza por el 0

print("The first planet is", planets[0])
print("The second planet is", planets[1])
print("The third planet is", planets[2])
planets[3] = "Red Planet"
print("Mars is also known as", planets[3])


# METODO len ES LA CANTIDAD DE ITEMS QUE TIENE LA LISTA

number_of_planets = len(planets)

print("There are", number_of_planets, "planets in the solar system.")

# OPERACIONES  DE VALORES DE LISTA
# Las listas de Python son dinámicas: puede agregar y quitar elementos después de crearlas. Para agregar un elemento a una lista, use el método .append(value).

# .append agrega un ITEM al final de la lista

# Por ejemplo, el código siguiente agrega la cadena "Pluto" al final de la lista planets:

planets.append("Pluto")
print(planets)
number_of_planets = len(planets)
print("There are actually", number_of_planets, "planets in the solar system.")
print("""
----->.append()  AÑADE UN ITEM AL FINAL DE LA LISTA<----
""")
print(planets)
 
# MÉTODO .pop.... quita el ultimo item de la lista



planets.pop()  # Goodbye, Pluto
number_of_planets = len(planets)
print("No, there are definitely", number_of_planets, "planets in the solar system.")

print("""
----->.pop() QUITA EL ULTIMO ITEM DE LA LISTA<----
""")
print(planets)


# Uso de índices negativos
# Ha visto cómo usar índices para capturar un elemento individual en una lista:

print("The first planet is", planets[0])

# Los índices comienzan en cero y van en aumento. Los índices negativos comienzan al final de la lista y van hacia atrás.

# En el ejemplo siguiente, un índice de -1 devuelve el último elemento de una lista. Un índice de -2 devuelve el penúltimo.

print("""
cuando el indice es negativo [-2] la lista se recorra de atrás hacia a adelante""")

print(planets)
print("The last planet is", planets[-1])
print("The penultimate planet is", planets[-2])


###### Uso de min() y max() con listas ######

# Python tiene funciones integradas para calcular los números más grandes y más pequeños de una lista. La función max() devuelve el número más grande y min() devuelve el más pequeño. Por lo tanto, min(gravity_on_planets) devuelve el número más pequeño de la lista gravity_on_planets, que es 0,377 (Marte).

# El código siguiente calcula los pesos mínimo y máximo en el sistema solar mediante esas funciones:

gravity_on_planets = [0.378, 0.907, 1, 0.377, 2.36, 0.916, 0.889, 1.12]


bus_weight = 12650 # in kilograms, on Earth

print("On Earth, a double-decker bus weighs", bus_weight, "kg")
print("The lightest a bus would be in the solar system is", bus_weight * min(gravity_on_planets), "kg")
print("The heaviest a bus would be in the solar system is", bus_weight * max(gravity_on_planets), "kg")

gravity_on_planets = [5.378, 6.907, 1, 1.377, 2.36, 0.916, 9.889, 0.12]

print(gravity_on_planets)
print(sorted(gravity_on_planets))
print(sorted(gravity_on_planets,reverse=True))


# SLICES

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
planets_before_earth = planets[0:2] # aquí e indica el rango de trabajo  es decir... queremos que se muestre la lista desde la posición 0 hasta la n-1 [n-1 = 2-1]
print(planets_before_earth)
# Output: ['Mercury', 'Venus']

# de igual forma si no  indicamos donde termina tomara en cuenta esta el ultimo item de la lista.

planets_after_earth = planets[3:]
print(planets_after_earth)

# Output
# ['Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

###############################################

# Combinación de listas
# Ha visto cómo puede usar segmentaciones para dividir listas, pero ¿qué sucede con unirlas de nuevo?

# Para unir dos listas, debe usar el otro operador (+) con dos listas para devolver una nueva.

amalthea_group = ["Metis", "Adrastea", "Amalthea", "Thebe"]
galilean_moons = ["Io", "Europa", "Ganymede", "Callisto"]

regular_satellite_moons = amalthea_group + galilean_moons
print("The regular satellite moons of Jupiter are", regular_satellite_moons)

# Output
# The regular satellite moons of Jupiter are ['Metis', 'Adrastea', 'Amalthea', 'Thebe', 'Io', 'Europa', 'Ganymede', 'Callisto']

# Ordenación de listas...

regular_satellite_moons.sort()
print("The regular satellite moons of Jupiter are", regular_satellite_moons)

# Output
# The regular satellite moons of Jupiter are ['Adrastea', 'Amalthea', 'Callisto', 'Europa', 'Ganymede', 'Io', 'Metis', 'Thebe']
regular_satellite_moons.sort(reverse=True)
print("The regular satellite moons of Jupiter are", regular_satellite_moons)

# Output
# The regular satellite moons of Jupiter are ['Thebe', 'Metis', 'Io', 'Ganymede', 'Europa', 'Callisto', 'Amalthea', 'Adrastea']