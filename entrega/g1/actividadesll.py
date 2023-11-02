# ACTIVIDADES GUÍA I.
# PARTE 2

# 8 
# Rectángulo
"""
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
"""


# 9
peso = float(input("Ingresa tu peso en kg: "))
estatura = float(input("Ingresa tu estatura en metros: "))
imc = peso / (estatura ** 2)
print(f"Tu índice de masa corporal es: {imc:.2f}")


# 10
celsius = float(input("Ingresa la temperatura en grados Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius} grados Celsius son equivalentes a {fahrenheit:.2f} grados Fahrenheit")



# 11
horas_trabajadas = float(input("Ingresa el número de horas trabajadas: "))
costo_por_hora = float(input("Ingresa el costo por hora: "))
sueldo = horas_trabajadas * costo_por_hora
print(f"El sueldo que te corresponde es: {sueldo}")


# 12
cantidad_invertida = float(input("Ingresa la cantidad a invertir: "))
interes_anual = float(input("Ingresa el interés anual en porcentaje: "))
cantidad_anios = int(input("Ingresa el número de años: "))
capital_obtenido = cantidad_invertida * (1 + interes_anual/100) ** cantidad_anios
print(f"El capital obtenido en la inversión es: {capital_obtenido:.2f}")


# 13
suma_precios = 0
for i in range(10):
    precio = float(input(f"Ingresa el precio del producto {i + 1}: "))
    suma_precios += precio

promedio = suma_precios / 10
print(f"El promedio de precios de los productos es: {promedio:.2f}")


# 14 
cadena_concatenada = 'Una ambiciosa' + ' Introducción' + ' a Python' + ' Parte 1'
print(cadena_concatenada)


# 15
sociedad = 'aiPython P1'
print(sociedad)
print(len(sociedad)) # imprime la variable "sociedad" con su longitud.
sociedad = sociedad.upper() # todos los caracteres pasan a mayúsculas
print(sociedad)
sociedad = sociedad.lower() # todos los caracteres pasan a minúsculas
print(sociedad)


# 16 
texto = "sometimes it is the people no one imagines anything of who do the things that no one can imagine."
texto_formateado = texto.capitalize()
print(texto_formateado)
texto_formateado = texto.title()
print(texto_formateado)
texto_formateado = texto.swapcase()
print(texto_formateado)


# 17
nombre_completo = input("Ingresa tu nombre completo: ")
print(nombre_completo * 3)

# Estos puntos no los entendí
# 18
# 19
# 20

# 21
palabra = input("Ingresa una palabra: ")
palabra = palabra.replace("a", "😃")
print(palabra)


# 22
frase = "El razonamiento matemático puede considerarse más bien esquemáticamente como el ejercicio de una combinación de dos instalaciones, que podemos llamar la intuición y el ingenio."
# cortar las dos primeras palabras
palabras = frase.split()
nueva_frase = ' '.join(palabras[2:])
print(nueva_frase)


# 23
frase2 = " La ciencia es una ecuación diferencial. La religión es una condición de frontera. "
frase_sin_espacios = frase2.strip()
print(frase_sin_espacios)


# 24
frase3 = "Usar el carácter de escape\ny nueva línea para separar la frase en dos líneas."
print(frase3)


# 25
tabla = "Nombre\tEdad\tPais\tCiudad\nAlexa\t250\tUSA\tCapeCod"
print(tabla)
