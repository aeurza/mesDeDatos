
# !Introducción a los diccionarios de Python

# Las variables de Python pueden almacenar varios tipos de datos. Anteriormente, ha aprendido que puede almacenar cadenas y números:
name = 'Earth'
moons = 1

# Aunque este método funciona para cantidades más pequeñas de datos, puede ser cada vez más complejo cuando se trabaja con datos relacionados. Imagine que quiere almacenar información sobre las lunas de la Tierra y la Luna.

earth_name = 'Earth'
earth_moons = 1

jupiter_name = 'Jupiter'
jupiter_moons = 79

# Observe cómo se duplican las variables con prefijos diferentes. Esta duplicación puede resultar difícil de manejar. Como con frecuencia tendrá que trabajar con conjuntos de datos relacionados, como el promedio de precipitaciones durante varios meses en distintas ciudades, almacenar estas variables como valores individuales no es una opción viable. Alternativamente, puede usar diccionarios de Python.

# Los diccionarios de Python permiten trabajar con conjuntos de datos relacionados. Un diccionario es una colección de pares clave-valor. Piense que es como un grupo de variables dentro de un contenedor, donde la clave es el nombre de la variable y el valor es el valor almacenado en su interior.

###########################
# !Creación de un diccionario

# Python usa llaves ({ }) y dos puntos (:) para indicar un diccionario. Puede crear un diccionario vacío y agregar valores más adelante, o bien rellenarlo en el momento de la creación. Cada clave o valor está separado por dos puntos y el nombre de cada clave se incluye entre comillas como un literal de cadena. Como la clave es un literal de cadena, puede usar el nombre que sea adecuado para describir el valor.

# Ahora se creará un diccionario para almacenar el nombre del planeta Tierra y el número de lunas que tiene:

planet = {
    'name': 'Earth',
    'moons': 1
}

# Tiene dos claves, 'name' y 'moons'. Cada clave se comporta igual que una variable: tienen un nombre único y almacenan un valor. Pero se incluyen dentro de una única variable más grande, denominada planet.

# Como sucede con las variables convencionales, debe asegurarse de que usa los tipos de datos correctos. En el valor moons de 1 en el ejemplo anterior, no se han incluido comillas alrededor del número, porque se quiere usar un entero. Si hubiera usado '1', Python vería esta variable como una cadena, lo que afectaría a la capacidad de realizar cálculos.

# # A diferencia de las variables convencionales, los nombres de clave no necesitan seguir las reglas de nomenclatura estándar para Python. Puede usar nombre clave para que sea más descriptivo en el código.


# __________________________________________________________

# !Lectura de valores de diccionario

# Puede leer valores dentro de un diccionario. Los objetos de diccionario tienen un método get que puede usar para acceder a un valor mediante su clave. Si quiere imprimir name, puede usar el código siguiente:


print(planet.get('name'))

# Displays Earth

# Como podría sospechar, el acceso a los valores de un diccionario es una operación común. Afortunadamente, hay un acceso directo. También puede pasar la clave entre corchetes ([ ]). Este método usa menos código que get y la mayoría de los programadores utilizan esta sintaxis en su lugar. Puede volver a escribir el ejemplo anterior mediante lo siguiente:

# planet['name'] is identical to using planet.get('name')
print(planet['name'])

# Displays Earth

# Aunque el comportamiento de get y los corchetes ([ ]) suele ser el mismo para recuperar elementos, hay una diferencia principal. Si una clave no está disponible, get devuelve None y [ ] genera un error KeyError.

wibble = planet.get('wibble') # * Returns None
# wibble = planet['wibble'] # * Throws KeyError

# !Modificación de valores de diccionario
# También puede modificar valores dentro de un objeto de diccionario, con el método update. Este método acepta un diccionario como parámetro y actualiza los valores existentes con los nuevos que proporcione. Si quiere cambiar name para el diccionario planet, puede usar lo siguiente, por ejemplo:

planet.update({'name': 'Makemake'})

# *name is now set to Makemake

# Al igual que se usa el acceso directo de corchetes ([ ]) para leer valores, se puede utilizar para modificar valores. La principal diferencia en la sintaxis es que se usa = (a veces denominado operador de asignación) para proporcionar un nuevo valor. Para volver a escribir el ejemplo anterior y cambiar el nombre, puede usar lo siguiente:

planet['name'] = 'Makemake'

# *name is now set to Makemake

# La principal ventaja de usar update es la capacidad de modificar varios valores en una operación. Los dos ejemplos siguientes son lógicamente los mismos, pero la sintaxis es diferente. Puede usar la sintaxis que crea más adecuada. La mayoría de los desarrolladores eligen corchetes para actualizar valores individuales.

# En el ejemplo siguiente se hacen las mismas modificaciones en la variable planet y se actualizan el nombre y las lunas. Tenga en cuenta que al usar update realiza una sola llamada a la función, mientras que el uso de corchetes implica dos llamadas.

# ?Using update
planet.update({
    'name': 'Jupiter',
    'moons': 79
})

# ?Using square brackets
planet['name'] = 'Jupiter'
planet['moons'] = 79

# !Adición y eliminación de claves

# No es necesario crear todas las claves al inicializar un diccionario. De hecho, no es necesario crear ninguna. Siempre que quiera crear una clave, asígnela como haría con una existente.

# Imagine que quiere actualizar planet para incluir el período orbital en días:


planet['orbital period'] = 4333

#* planet dictionary now contains: {
#*   name: 'jupiter'
#*   moons: 79
#*   orbital period: 4333
#* }

# Para quitar una clave, use pop. pop devuelve el valor y quita la clave del diccionario. Para quitar orbital period, puede usar el código siguiente:

planet.pop('orbital period')

#* planet dictionary now contains: {
#*   name: 'jupiter'
#*   moons: 79
#* }

# !Tipos de data complejos
# Los diccionarios pueden almacenar cualquier tipo de valor, incluidos otros diccionarios. Esto le permite modelar datos complejos según sea necesario. Imagine que tiene que almacenar el diámetro de planet, que se podría medir alrededor de su ecuador o los polos. Puede crear otro diccionario dentro de planet para almacenar esta información:

#* Add address
planet['diameter (km)'] = {
    'polar': 133709,
    'equatorial': 142984
}

#* planet dictionary now contains: {
#*   name: 'Jupiter'
#*   moons: 79
#*   diameter (km): {
#*      polar: 133709
#*      equatorial: 142984
#*   }
#* }


# Para recuperar valores en un diccionario anidado, debe encadenar corchetes o llamadas a get.

print(f'{planet["name"]} polar diameter: {planet["diameter (km)"]["polar"]}')
#* Output: Jupiter polar diameter: 133709ls

# !Programación dinámica con diccionarios


# En el programa, quiere realizar varios cálculos, como el del número total de lunas. Además, a medida que progrese en programación más avanzada, es posible que compruebe que carga este tipo de información desde archivos o una base de datos, en lugar de programar directamente en Python.

# Para ayudar a admitir estos escenarios, Python le permite tratar las claves y los valores dentro de un diccionario como una lista. Puede determinar de manera dinámica las claves y los valores, y realizar varios cálculos.

# Imagine un diccionario en el que se almacenan cantidades mensuales de precipitaciones. Es probable que tenga claves para cada mes y las precipitaciones asociadas. Quiere sumar el total de precipitaciones y escribir el código para realizar la operación mediante cada clave individual sería bastante tedioso.
# !Recuperación de todas las claves y valores

# El método keys() #devuelve un objeto de lista que contiene todas las claves. Puede usar este método para iterar por todos los elementos del diccionario.

# Imagine que tiene el siguiente diccionario, en el que se almacenan los últimos tres meses de precipitaciones.

rainfall = {
    'october': 3.5,
    'november': 4.2,
    'december': 2.1
}

# Imagine que quiere mostrar la lista de todas las precipitaciones. Puede escribir el nombre de cada mes, pero resultará tedioso.

for key in rainfall.keys():
    print(f'{key}: {rainfall[key]}cm')

# Output:
# october: 3.5cm
# november: 4.2cm
# december: 2.1cm

# !Determinación de la existencia de una clave en un diccionario

# Al actualizar un valor en un diccionario, Python sobrescribirá el valor existente o creará uno, si la clave no existe. Si quiere agregar a un valor en lugar de sobrescribirlo, puede comprobar si la clave existe mediante in. Por ejemplo, si quiere agregar un valor a diciembre o crear uno si no existe, puede usar lo siguiente:

if 'december' in rainfall:
    rainfall['december'] = rainfall['december'] + 1
else:
    rainfall['december'] = 1

#* Because december exists, the value will be 3.1

# !Recuperación de todos los valores

# De forma similar a keys(), values() devuelve la lista de todos los valores de un diccionario sin sus claves correspondientes. values() puede resultar útil cuando se usa la clave con fines de etiquetado, como en el ejemplo anterior, en el que las claves son el nombre del mes. Puede usar para values() determinar el importe total de las precipitaciones:


total_rainfall = 0
for value in rainfall.values():
    total_rainfall = total_rainfall + value

print(f'There was {total_rainfall}cm in the last quarter')

# *Output:
# *There was 10.8cm in the last quarter

