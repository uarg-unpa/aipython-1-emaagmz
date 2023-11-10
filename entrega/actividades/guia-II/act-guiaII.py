# ACTIVIDADES GUÍA II

# 1
edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Tiene edad suficiente para conducir.")
else:
    print(f"Faltan {18 - edad} años para poder conducir.")


# 2
mi_edad = 22 
tu_edad = int(input("Ingrese su edad: "))
if tu_edad > mi_edad:
    diferencia = tu_edad - mi_edad
    if diferencia == 1:
        print(f"Eres mayor que yo por 1 año.")
    else:
        print(f"Eres mayor que yo por {diferencia} años.")
elif tu_edad < mi_edad:
    print(f"Soy mayor que tú por {mi_edad - tu_edad} años.")
else:
    print("¡Somos de la misma edad! ¡Qué coincidencia!")


# 3
contrasena_guardada = "contrasena123" 
contrasena_ingresada = input("Ingrese su contraseña: ")
if contrasena_ingresada.lower() == contrasena_guardada.lower():
    print("¡La contraseña es correcta!")
else:
    print("La contraseña no coincide.")


# 4
a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
if a > b:
    print(f"{a} es mayor que {b}.")
elif a < b:
    print(f"{a} es menor que {b}.")
else:
    print(f"{a} es igual a {b}.")

# 5
numero = int(input("Ingrese un número entero: "))
if numero % 2 == 0:
    print(f"{numero} es un número par.")
else:
    print(f"{numero} es un número impar.")

# 6
numero_dia = int(input("Ingrese un número del 1 al 7: "))
dias_semana = ["", "lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
if 1 <= numero_dia <= 7:
    print(f"Corresponde a {dias_semana[numero_dia]}.")
else:
    print("Número fuera de rango. Debe ser del 1 al 7.")

# 7
puntuacion = int(input("Ingrese la puntuación del estudiante: "))
if 80 <= puntuacion <= 100:
    print("A")
elif 70 <= puntuacion <= 89:
    print("B")
elif 60 <= puntuacion <= 69:
    print("C")
elif 50 <= puntuacion <= 59:
    print("D")
elif 0 <= puntuacion <= 49:
    print("F")
else:
    print("Puntuación fuera de rango. Debe ser entre 0 y 100.")

# 8 
edad_cliente = int(input("Ingrese la edad del cliente: "))
if edad_cliente < 4:
    print("El cliente puede entrar gratis.")
elif 4 <= edad_cliente <= 18:
    print("El cliente debe pagar $5.")
else:
    print("El cliente debe pagar $10.")

# 9
edad_usuario = int(input("Ingrese su edad: "))
ingresos_mensuales = float(input("Ingrese sus ingresos mensuales: "))
if edad_usuario > 18 and ingresos_mensuales >= 100000:
    print("Debe pagar el impuesto.")
else:
    print("No tiene que pagar el impuesto.")


"""
promedio = 0
cont = 0
suma = 0

while(cont < 3):
    nota = int(input("Ingrese la nota: "))
    suma = suma + nota
    cont = cont + 1

promedio = suma / 3
print(f"El promedio de las notas es: {promedio:.2f}")
"""