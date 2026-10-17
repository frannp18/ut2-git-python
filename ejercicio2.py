nota = int(input("Introduce tu nota: "))

if (nota < 0 or nota > 10):
	print("Nota no válida")
elif (nota < 5):
    	print("Insuficiente")
>>>>>>> validar-nota
elif (nota >= 5 and nota < 7):
    	print("Estás aprobado")
elif (nota >= 7 and nota < 9):
    	print("Tienes un notable")
else:
    	print("Tienes un sobresaliente")