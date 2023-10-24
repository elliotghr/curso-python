"""Ejercicio 1

Crear un programa que tenga una lista, luego crear una funcion con la cual se van a pedir numeros al usuario para agregar a la lista. Debes crear una segunda funcion en donde se ordenen los numeros pares e impares dentro de dos listas nuevas"""

numbers = []

def pedir():
    i = 1
    while i < 6:
        number = int(input("Ingresa un numero: "))
        numbers.append(number)
        i += 1
    print(numbers)

def ordenar():
    par = []
    impar = []
    numbers.sort()
    # print(numbers)
    for item in numbers:
        if item % 2 == 0:
            par.append(item)
        else:
            impar.append(item)
    print(par)
    print(impar)

pedir()
ordenar()