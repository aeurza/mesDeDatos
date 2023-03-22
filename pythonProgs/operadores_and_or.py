# Los operadores [and] y  [or] nos permiten dar lógica a una sentencia
# es decir que operamos de manera BOLEANA

print("Introduce una par de números que estén entre 25 y 35.")
print("Si logras averiguar el número secreto de hoy te mostraremos la suma de los 2 números que introduciste. Caso contrario sigue intentando")
print("Good luck!")

a =  int(input("Introduce un 1er número: "))
b =  int(input("Introduce un 2er número: "))
c =  34

if 25 <= a <= 35 and 25 <= b <= 35:
    if a ==  c or b == c :
        print(a + b)
        print("Felicidades si adivinaste el número")
    else:
        print("Lo siento mucho no adivinas te el número de hoy")
        print("Inténtalo de nuevo")
else:
    print("Error, ingresa números entre 25-35")