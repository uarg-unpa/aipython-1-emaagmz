# ACTIVIDADES GUÍA III

# 1
i = 0
while i <= 100:
    print(i)
    i += 1

# 2
for i in range(101):
    print(i)

# 3
i = 10
while i >= 0:
    print(i)
    i -= 1

# 4
numero1 = int(input("Ingrese el primer número entero: "))
numero2 = int(input("Ingrese el segundo número entero: "))
for i in range(numero1, numero2 + 1):
    print(i)

# end=' '

# 5
for i in range(1, 8):
    print("#" * i)

# 6
for i in range(8):
    for j in range(8):
        print("#", end="")
    print()

# 7
nombre_usuario = input("Ingrese su nombre de usuario: ")
numero_repeticiones = int(input("Ingrese un número entero: "))
for _ in range(numero_repeticiones):
    print(nombre_usuario)

# 8
numero_limite = int(input("Ingrese un número entero mayor a 3: "))
for i in range(1, numero_limite + 1, 2):
    print(i)

# 9
for i in range(11):
    resultado = i * i
    print(f"{i} x {i} = {resultado}")

# 10
for i in range(7):
    for j in range(i, 7):
        print(f"{i} {j}")

# 11
numero_filas = int(input("Ingrese un número entero: "))
for i in range(numero_filas, 0, -2):
    for j in range(i, 0, -2):
        print(j, end=" ")
    print()

# 12
num_natural = int(input("Ingrese un número natural N: "))
suma = 0
for i in range(1, num_natural + 1):
    suma += i
    if i == num_natural:
        print(f"{i} = {suma}")
    else:
        print(f"{i} +", end=" ")

# 13
num_nat = int(input("Ingrese un número natural N: "))
suma_pares = 0
for i in range(2, 2*num_nat + 1, 2):
    suma_pares += i
print(f"La suma de los primeros {num_nat} números pares es: {suma_pares}")

# 14
inicio = int(input("Ingrese el primer número entero: "))
fin = int(input("Ingrese el segundo número entero: "))
for num in range(inicio, fin + 1):
    if num % 2 == 0:
        print(num)

# 15
inicio = int(input("Ingrese el primer número entero: "))
fin = int(input("Ingrese el segundo número entero: "))
for num in range(inicio, fin + 1):
    if num % 2 == 0:
        print(num)
 