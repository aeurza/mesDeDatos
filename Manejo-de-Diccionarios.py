
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
#* Output: Jupiter polar diameter: 133709