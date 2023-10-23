"""Ejercicio 2

Pedir al usuario que ingrese 2 numeros, después, se debe mostrar el rango de esos 2 números, pero, solo imprimiendo los números que sean impares"""

first = int(input("Ingresa el primer valor: "))
last = int(input("Ingresa el segundo valor: "))

for x in range(first, last + 1):
    if not x % 2 == 0:
        print(x)
