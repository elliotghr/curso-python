"""Ejercicio 2

Escribe una lista que tenga los números de 1 al 10. Luego, debes hacer que los datos que están en las posiciones 4, 7 y 9 sean multiplicados por 2; por último, mostrar la lista nueva con los nuevos datos"""

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

positions = [4, 7, 9]

for position in positions:
    lista[position] = lista[position] * 2

print(lista)
