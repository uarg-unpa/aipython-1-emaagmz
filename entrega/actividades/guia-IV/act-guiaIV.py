# ACTIVIDADES GUÍA IV
# 1
lista_vacia = []

# 2
lista_mas_7 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 3
long_lista_mas_7 = len(lista_mas_7)
print("Longitud de la lista_mas_7:", long_lista_mas_7)

# 4
frutas_favoritas = ["manzana", "banana", "uva", "mandarina", "sandía"]
# a
print("Longitud de frutas_favoritas:", len(frutas_favoritas))
# b
frutas_favoritas.pop(0)
# c
frutas_favoritas.append("naranja")
# d
print("Frutas después de las operaciones:", frutas_favoritas)

# 5
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Primer elemento:", lista_numeros[0])
print("Elemento del medio:", lista_numeros[len(lista_numeros)//2])
print("Último elemento:", lista_numeros[-1])

# 6
datos_personales = ["Emanuel", 22, 1.79, "Soltero", "Mi dirección"]

# 7
companias_favoritas = ["MercadoLibre", "Apple", "Microsoft"]

# 8
for dato in datos_personales:
    print(dato)

# 9
for i, compania in enumerate(companias_favoritas):
    print(f"Índice {i}: {compania}")

# 10
companias_favoritas[0] = "Amazon"
print("Lista de compañías después de la modificación:", companias_favoritas)

# 11
numeros_1_al_10 = list(range(1, 11))
# a
print("Tres primeros números:", numeros_1_al_10[:3])

# 12
letras_a_j = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
# a
print("Cada segundo elemento:", letras_a_j[1::2])

# 13
lista_criterio = [10, 20, 30, 40, 50]
# a
print("Lista en forma inversa:", lista_criterio[::-1])

# 14
palabras_favoritas = ["Código", "Python", "Programación", "Desarrollo", "Creatividad"]
# a
sublista_palabras = palabras_favoritas[1:4]
print("Sublista de palabras:", sublista_palabras)

# 15
flores = ["rosas", "orquídea", "lirio", "tulipan", "margarita", "dalia", "hortensia"]
# a
print("Tres elementos desde el tercer elemento:", flores[2:5])
# b
print("Elementos en posiciones pares desde la segunda posición:", flores[1::2])
# c
print("Elementos desde la primera posición saltando de a tres elementos:", flores[::3])
