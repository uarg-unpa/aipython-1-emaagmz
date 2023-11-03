promedio = 0
cont = 0
suma = 0

while(cont < 3):
    nota = int(input("Ingrese la nota: "))
    suma = suma + nota
    cont = cont + 1

promedio = suma / 3
print(f"El promedio de las notas es: {promedio:.2f}")