# Introducción
# Completado
# 100 XP
# 1 minuto
# Las cadenas de Python son uno de los tipos más importantes y más comunes del lenguaje. Aprender a interactuar con las cadenas, incluido el formato y el reemplazo de texto, es una aptitud esencial que se debe desarrollar para trabajar con código de Python.

# Escenario: Creación de un programa para describir hechos sobre la Luna
# # Imagine que va a crear un programa para describir algunas medidas y otra información sobre la Luna. Tendrá que usar varias operaciones de cadena para crear la salida.


###### Para manejar str en python debemos tomar en cuenta ciertas consideraciones:
    # por ejemplo es mejor usa COMILLAS DOBLES, cuando queremos introducir texto para que no entre en conflicto cone el uso de las apostrofes si es que la necesitáramos usar.

# >>> 'We only see about 60% of the Moon's surface'
#   File "<stdin>", line 1
    # 'We only see about 60% of the Moon's surface'
                                    #    ^
# SyntaxError: invalid syntax
#####################################################


# Texto multilínea
# Hay diferentes maneras de definir varias líneas de texto como una sola variable. Las más comunes son las siguientes:

# Usar un carácter de nueva línea (\n).
# Usar comillas triples (""").

# multiline = "Facts about the Moon:\n There is no atmosphere.\n There is no sound."

# print(multiline)

# comillas ="""Facts about the Moon:
#     There is no atmosphere.
#     There is no sound."""

# print(comillas)

head = "esta es una cadena para el método .title"

head.title()
print(head)

# split por espacios
head.split("")
[esta, es, una, cadena, para, el, metodo, .title]




# split por lineas
head1 = """asd
    qwe
    zxc"""
head1.split("\n")
[asd, qwe, zxc]


print(head)

# busqueda en una cadena usaremos [in]

>>> "Moon" in "This text will describe facts and challenges with space travel"
False
>>> "Moon" in "This text will describe facts about the Moon"
True

# Un enfoque para buscar la posición de una palabra específica en una cadena consiste en usar el método .find():

>>> temperatures = """Saturn has a daytime temperature of -170 degrees Celsius,
... while Mars has -28 Celsius."""
>>> temperatures.find("Moon")
-1

# El método .find() devuelve -1 cuando no se encuentra la palabra, o bien devuelve el índice (el número que representa la posición en la cadena). Así es como se comportaría si busca la palabra Mars:

>>> temperatures.find("Mars")
65
# 65 es la posición donde "Mars" aparece en la cadena.

############################
# Otra manera de buscar contenido consiste en usar el método .count(), que devuelve el número total de repeticiones de una palabra determinada en una cadena:

>>> temperatures.count("Mars")
1
>>> temperatures.count("Moon")
0

>>> mars_temperature = "The highest temperature on Mars is about 30 C"
>>> for item in mars_temperature.split():
...     if item.isnumeric():
...         print(item)
...
30

 Importante

Le sorprenderá saber que "-70".isnumeric() devolverá False. Esto se debe a que todos los caracteres de la cadena tendrían que ser numéricos y el guión (-) no lo es. Si tiene que comprobar números negativos en una cadena, el método .isnumeric() no funcionará.

>>> "-60".startswith('-')
True

De forma similar, el método .endswith() ayuda a comprobar el último carácter de una cadena:

>>> if "30 C".endswith("C"):
    print("This temperature is in Celsius")
'This temperature is in Celsius'



############
Es posible que no tenga que realizar la comprobación sin distinguir mayúsculas de minúsculas todo el tiempo, pero convertir en minúsculas todas las letras es un buen enfoque cuando en el texto se usa una mezcla de mayúsculas y minúsculas.

Después de dividir el texto y realizar las transformaciones, es posible que tenga que volver a ensamblar todas las piezas. Al igual que el método .split() puede separar caracteres, el método .join() puede volver a agruparlos.

El método .join() necesita un elemento iterable (como una lista de Python) como argumento, por lo que su uso es diferente al de otros métodos de cadena:

>>> moon_facts = ["The Moon is drifting away from the Earth.", "On average, the Moon is moving about 4cm every year"]
>>> '\n'.join(moon_facts)
'The Moon is drifting away from the Earth.\nOn average, the Moon is moving about 4cm every year'





