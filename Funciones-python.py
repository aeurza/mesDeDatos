
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

# ?rocket_parts()
# ?'payload, propellant, structure'

# La función rocket_parts() no toma ningún argumento e imprime una instrucción sobre la gravedad. Si necesita usar un valor que devuelve una función, puede asignar la salida de la función a una variable:

output = rocket_parts()
payload, propellant, structure
output is None
True



# Puede parecer sorprendente que el valor de la variable output sea None. Esto se debe a que la función rocket_parts() no ha devuelto explícitamente un valor. En Python, si una función no devuelve explícitamente un valor, devuelve implícitamenteNone. Actualizar la función para devolver la cadena en lugar de imprimirla hace que la variable output tenga un valor distinto:

>>> def rocket_parts():
...     return "payload, propellant, structure"
...
>>> output = rocket_parts()
>>> output
'payload, propellant, structure'

# !Argumentos opcionales y requeridos

# En Python, varias funciones integradas requieren argumentos. Algunas funciones integradas hacen que los argumentos sean opcionales. Las funciones integradas están disponibles de inmediato, por lo que no es necesario importarlas explícitamente.

# Un ejemplo de una función integrada que requiere un argumento es any(). Esta función toma un objeto iterable (por ejemplo, una lista) y devuelve True si algún elemento del objeto iterable es True. De lo contrario, devuelve False.

>>> any([True, False, False])
True
>>> any([False, False, False])
False

# Si llama a any() sin ningún argumento, se genera una excepción útil. El mensaje de error explica que necesita al menos un argumento:

>>> any()
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
TypeError: any() takes exactly one argument (0 given)

# Puede comprobar que algunas funciones permiten el uso de argumentos opcionales mediante otra función integrada denominada str(). Esta función crea una cadena a partir de un argumento. Si no se pasa ningún argumento, devuelve una cadena vacía:

>>> str()
''
>>> str(15)
'15'

# !Uso de argumentos de función en Python

# Ahora que sabe cómo crear una función sin entradas, el paso siguiente es crear funciones que requieran un argumento. El uso de argumentos hace que las funciones sean más flexibles, ya que pueden hacer más y condicionalizar lo que hacen.

# !Exigencia de un argumento

# Si va a pilotar un cohete, una función sin entradas obligatorias es como un equipo con un botón que le indique la hora. Si presiona el botón, una voz computarizada le indicará la hora. Pero una entrada necesaria puede ser un destino para calcular la distancia del viaje. Las entradas obligatorias se denominan argumentos para la función.

# Para requerir un argumento, póngalo entre paréntesis:

def distance_from_earth(destination):
    if destination == "Moon":
        return "238,855"
    else:
        return "Unable to compute to that destination"

# Intente llamar a la función distance_from_earth() sin ningún argumento:

>>> distance_from_earth()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: distance_from_earth() missing 1 required positional argument: 'destination'


# Python genera TypeError con un mensaje de error que indica que la función requiere un argumento denominado destination. Si se pide al equipo del cohete que calcule la distancia del viaje con un destino, debe solicitar que un destino es un requisito. El código de ejemplo tiene dos rutas de acceso para una respuesta, una para la Luna y la otra para cualquier otra cosa. Use la Luna como entrada para obtener una respuesta

>>> distance_from_earth("Moon")
'238,855'

# Dado que hay una condición catch-all, intente usar cualquier otra cadena como destino para comprobar ese comportamiento:

>>> distance_from_earth("Saturn")
'Unable to compute to that destination'


# !Varios argumentos necesarios
# Para usar varios argumentos, debe separarlos con una coma. Vamos a crear una función que pueda calcular cuántos días se tardarán en llegar a un destino, dadas la distancia y una velocidad constante:


def days_to_complete(distance, speed):
    hours = distance/speed
    return hours/24

# Ahora use la distancia entre la Tierra y la Luna para calcular cuántos días tardaría en llegar a la Luna con un límite de velocidad común de 120 kilómetros por hora:

>>> days_to_complete(238855, 75)
132.69722222222222

# !Funciones como argumentos

# Puede usar el valor de la función days_to_complete() y asignarlo a una variable y, después, pasarlo a round() (una función integrada que redondea al número entero más cercano) para obtener un número entero:

>>> total_days = days_to_complete(238855, 75)
>>> round(total_days)
133

# Pero un patrón útil es pasar funciones a otras funciones en lugar de asignar el valor devuelto:

>>> round(days_to_complete(238855, 75))
133

#  ^Sugerencia

# ^Aunque pasar funciones directamente a otras funciones como entrada es útil, existe la posibilidad de que se reduzca la legibilidad. Este patrón es especialmente problemático cuando las funciones requieren muchos argumentos.
# !Uso de argumentos de palabra clave en Python

# Los argumentos opcionales requieren un valor predeterminado asignado a ellos. Estos argumentos con nombre se denominan argumentos de palabra clave. Los valores del argumento de palabra clave deben definirse en las propias funciones. Cuando se llama a una función definida con argumentos de palabra clave, no es necesario usarlos en absoluto.

# La misión Apolo 11 tardó unas 51 horas en llegar a la Luna. Vamos a crear una función que devuelva la hora estimada de llegada usando el mismo valor que la misión Apolo 11 como valor predeterminado:


from datetime import timedelta, datetime

def arrival_time(hours=51):
    now = datetime.now()
    arrival = now + timedelta(hours=hours)
    return arrival.strftime("Arrival: %A %H:%M")

# La función usa el módulo datetime para definir la hora actual. Usa timedelta para permitir la operación de suma que da como resultado un objeto de hora nuevo. Después de calcular ese resultado, devuelve la estimación arrival con formato de cadena. Intente llamarla sin ningún argumento:

>>> arrival_time()
'Arrival: Saturday 16:42'


# Aunque la función define un argumento de palabra clave, no permite pasar uno cuando se llama a una función. En este caso, la variable hours tiene como valor predeterminado 51. Para comprobar que la fecha actual es correcta, use 0 como valor para hours:

>>> arrival_time(hours=0)
'Arrival: Thursday 13:42'

# !Combinación de argumentos y argumentos de palabra clave

# A veces, una función necesita una combinación de argumentos de palabra clave y argumentos. En Python, esta combinación sigue un orden específico. Los argumentos siempre se declaran primero, seguidos de argumentos de palabra clave.

# Actualice la función arrival_time() para que tome un argumento necesario, que es el nombre del destino:

from datetime import timedelta, datetime

def arrival_time(destination, hours=51):
    now = datetime.now()
    arrival = now + timedelta(hours=hours)
    return arrival.strftime(f"{destination} Arrival: %A %H:%M")

# Dado que ha agregado un argumento necesario, ya no es posible llamar a la función sin ningún argumento:

>>> arrival_time()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: arrival_time() missing 1 required positional argument: 'destination'

# Use "Moon" como valor para destination a fin de evitar el error:

>>> arrival_time("Moon")
'Moon Arrival: Saturday 16:54'

# También puede pasar más de dos valores, pero debe separarlos con una coma. Se tarda aproximadamente 8 minutos (0,13 horas) en entrar en órbita, así que utilice eso como argumento:

>>> arrival_time("Orbit", hours=0.13)
'Orbit Arrival: Thursday 14:11'

# !Uso de argumentos de variable en Python

# En Python, puede usar cualquier número de argumentos de palabra clave y argumentos sin necesidad de declarar cada uno de ellos. Esta capacidad es útil cuando una función puede obtener un número desconocido de entradas.

# !Argumentos de variable

# Los argumentos en las funciones son necesarios. Pero cuando se usan argumentos de variable, la función permite pasar cualquier número de argumentos (incluido 0). La sintaxis para usar argumentos de variable es agregar un asterisco único como prefijo (*) antes del nombre del argumento.

# La función siguiente imprime los argumentos recibidos:

def variable_length(*args):
    print(args)

# ^Nota

# ^No es necesario denominar a los argumentos de variable args. Puede usar cualquier nombre de variable válido. Aunque es habitual ver *args o *a, debe intentar usar la misma convención en un proyecto.