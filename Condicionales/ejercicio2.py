"""Ejercicio 2

Escribir un programa que, dado un número entero, muestre su valor absoluto. 
Nota: para los números positivos su valor absoluto es igual al número (el valor absoluto de 52 es 52), mientras que, para los negativos, su valor absoluto es el número multiplicado por -1 (el valor absoluto de -52 es 52)."""

word = int(input("Ingresa un número entero: "))
print(type(word))
if type(word) == "int":
    print(abs(word))
else:
    print("No es un número")
