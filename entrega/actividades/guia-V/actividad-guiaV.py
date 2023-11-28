# ACTIVIDADES GUÍA V
# 1
def multiplicar(a, b):
    return a * b

# 2
def multiplicar_con_predeterminado(a=1, b=1):
    return a * b

# 3
def msj_creativo(nombre):
    return f"Hola {nombre}, ¡bienvenido a la creatividad!"

# 4
def tabla_multiplicar(numero):
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

# 5
def par_o_impar(numero):
    if numero % 2 == 0:
        return "Par"
    else:
        return "Impar"

# 6
def factorial(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * factorial(numero - 1)

# 7
def maximo_de_tres(a, b, c):
    return max(a, b, c)

# 8
def invertir_string(texto):
    return texto[::-1]

# 9
def multiplicar_lista(lista):
    resultado = 1
    for elemento in lista:
        resultado *= elemento
    return resultado

# 10
def es_palindromo(palabra):
    palabra = palabra.lower().replace(" ", "")
    return palabra == palabra[::-1]

# 11
def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# 12
def contador_vocales(lista):
    vocales = "aeiouAEIOU"
    cantidad = 0
    for caracter in lista:
        if caracter in vocales:
            cantidad += 1
    return cantidad

# 13
def intercalar_listas(lista1, lista2):
    intercalada = []
    for elemento1, elemento2 in zip(lista1, lista2):
        intercalada.append(elemento1)
        intercalada.append(elemento2)
    return intercalada

# 14
def promedio_lista(lista):
    if not lista:
        return None
    return sum(lista) / len(lista)


print(multiplicar(5, 4))
print(multiplicar_con_predeterminado())
print(msj_creativo("Programador"))
tabla_multiplicar(8)
print(par_o_impar(7))
print(factorial(5))
print(maximo_de_tres(7, 2, 9))
print(invertir_string("Programación"))
print(multiplicar_lista([1, 2, 3, 4]))
print(es_palindromo("Safas"))
print(fahrenheit_a_celsius(32))
print(contador_vocales(['a', 'b', 'c', 'd', 'e', 'f']))
print(intercalar_listas([1, 2, 3], ['a', 'b', 'c']))
print(promedio_lista([1, 2, 3, 4, 5]))
