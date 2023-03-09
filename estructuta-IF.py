# En este programa veremos el empleo de la estructura IF

# Es igual que: a == b
# No es igual a: a != b
# Menor que: a < b
# Menor o igual que: a <= b
# Mayor que: a > b
# Mayor o igual que: a >= b


# here i declare the vars

a = input("Introduzca un primer número: ")
b =  input("Introduzca un segundo número: ")

if a < b:
    print(b)


if a >= b:
    print(a)
else:
    print(b)


if a >= b:
    print("a is grater than or equal to b")
elif a == b:
    print("a is equal to b")


if a > b:
    print("a is greater than b")
elif a < b:
    print("a is less than b")
else: 
    print ("a is equal to b")  

    



