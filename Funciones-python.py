
# !Introducción

# El uso de una función de Python es el primer paso para codificar después de las estructuras de datos y los condicionales básicos. Las funciones permiten la reutilización, lo que evita la duplicación de código. Cuando los proyectos reutilizan código con funciones, se vuelven más legibles y fáciles de mantener.

# Escenario: Organización de datos sobre un cohete
# Imagine va a crear un programa para construir información precisa sobre un cohete espacial. Las funciones reutilizables le permitirán no solo calcular información, sino también crear valores combinando entradas y salidas de otras funciones.

# ¿Qué descubriré?
# En este módulo, aprenderá a:

# Usar entradas predeterminadas, obligatorias y de carácter comodín.
# Hacer que el código sea reutilizable extrayendo patrones comunes en funciones independientes.
# Devolver valores, estructuras de datos o resultados calculados.
# ¿Cuál es el objetivo principal?
# Al final de este módulo, comprenderá algunas de las reglas y el comportamiento asociado a las funciones, incluida la forma de controlar las entradas y salidas.


# !Funciones sin argumentos

# Para crear una función, use la palabra clave def, seguida de un nombre, paréntesis y, después, del cuerpo con el código de función

def rocket_parts():
    print("payload, propellant, structure")

    # En este caso, rocket_parts es el nombre de la función. Ese nombre va seguido de paréntesis vacíos, que indican que no se necesitan argumentos. El último es el código, con sangría de cuatro espacios. Para usar la función, debe llamarla por su nombre usando paréntesis:

rocket_parts()
'payload, propellant, structure'

# La función rocket_parts() no toma ningún argumento e imprime una instrucción sobre la gravedad. Si necesita usar un valor que devuelve una función, puede asignar la salida de la función a una variable:

output = rocket_parts()
payload, propellant, structure
output is None
True