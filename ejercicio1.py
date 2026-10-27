#Autor: Compañero
try:
    num = int(input("Introduce un número: "))
except ValueError:
    print("Error: debes introducir un número entero")
else:
    iff num % 2 == 0:
        print(num, "es par")
    else:
        print(num, "es impar")