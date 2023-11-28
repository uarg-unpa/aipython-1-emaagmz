nombres = ["nombre1", "nombre2", "nombre3"]

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(len(numeros))

for elementos in numeros:
    print(elementos, end=", ")

"""numeros[8] = 10
print(numeros)"""

numeros.append(10)
print(numeros)

lista = [20,30,30,30,40, 50]
lista.remove(30)
print(lista)

lista.pop()
print(lista)

lista.reverse()
print(lista)

print(["actividad", "guia", "guia"].count("guia"))

lista2 = [5,-10,35,0,-65,100]
lista2.sort()
print(lista2)

del(lista2[0])
print(lista2)