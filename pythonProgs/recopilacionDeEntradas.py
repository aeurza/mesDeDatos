# importamos el modulo [sys] con el fin de te poder introducir argumentos desde la linea de comandos


import sys
nameProg = sys.argv[0]
countArgs = len(sys.argv)
arguments = str(sys.argv)

print("Nombre del Prog:{}".format(nameProg))
print("Cantidad de argumentos: {}".format(countArgs))
print("lista de argumentos {}".format(arguments))

# At the begging  oh the program i run a greeting in order to say hello

print("Welcome to the greeter program")
name = input("Enter your name: ")
print("Greetings " + name)

# then I will request to the user 2 number to sum  them and show the result

print("Now, " + name)
print("I will sum 2 numbers for you, Would you give me some?")

a = input("Type the first one: ")
b = input("Type the second one: ")
sol1 = int(a) + int(b)
print("The result is: " + str(sol1))

