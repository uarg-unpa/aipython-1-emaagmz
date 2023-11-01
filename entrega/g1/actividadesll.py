# ACTIVIDADES GUÍA I.
# PARTE 2

# 8 
# Rectángulo
base = float(input("Ingresa la base del rectángulo: "))
altura = float(input("Ingresa la altura del rectángulo: "))
perimetro_rectangulo = 2 * (base + altura)
area_rectangulo = base * altura
print(f"Perímetro del rectángulo: {perimetro_rectangulo}")
print(f"Área del rectángulo: {area_rectangulo}")
# circunferencia
radio = float(input("Ingresa el radio de la circunferencia: "))
pi = 3.14159  # valor aproximado de pi
perimetro_circunferencia = 2 * pi * radio
area_circunferencia = pi * radio ** 2
print(f"Perímetro de la circunferencia: {perimetro_circunferencia}")
print(f"Área de la circunferencia: {area_circunferencia}")


# 9
peso = float(input("Ingresa tu peso en kg: "))
estatura = float(input("Ingresa tu estatura en metros: "))
imc = peso / (estatura ** 2)
print()


# 10



# 11
horas_trabajadas = float(input("Ingresa el número de horas trabajadas: "))
costo_por_hora = float(input("Ingresa el costo por hora: "))
sueldo = horas_trabajadas * costo_por_hora
print(f"El sueldo que te corresponde es: {sueldo}")
