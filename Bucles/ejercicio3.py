"""Ejercicio 1

Imprimir por pantalla los numeros del 1 al 10, luego, pedir al usuario dos numeros y mostrar el rango de numeros entre ambas cifras

"""

for x in range(1, 11):
    print(x)

first = int(input("Ingresa el primer valor: "))
last = int(input("Ingresa el segundo valor: "))

for x in range(first, last + 1):
    print(x)
