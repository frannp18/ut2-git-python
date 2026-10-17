nota = int(input("Introduce tu nota: "))

if (nota < 5):
    print("Insuficiente")
elif (nota >= 5 and nota < 7):
    print("Estás aprobado")
elif (nota >= 7 and nota < 9):
    print("Tienes un notable")
else:
    print("Tienes un sobresaliente")