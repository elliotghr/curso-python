"""Ejercicio 1

Escribir un programa que pida un numero al usuario y muestre las tablas de multiplicar de ese numero
"""

multiplicador = int(input("Escribe un número: "))

i = 0
while i < 10:
    i += 1
    print(f"{i} x {multiplicador} = {i*multiplicador}")
