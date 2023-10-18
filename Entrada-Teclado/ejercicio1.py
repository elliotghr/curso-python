"""
Ejercicio 1

Realizar un programa que haga el proceso de formula general para la resolución de ecuaciones, sabiendo que la formula general es la que está en la imagen, el usuario debe ingresar los valores de “a”, “b” y “c”, y el programa debe hacer el proceso para que al final muestre el mensaje: “La solución es: <solucion>”
Formula: ax2+bx+c=0
"""

from math import sqrt

print("Para ejecutar la formula general necesitaremos 3 valores.")
a = int(input("Ingresa el valor para a: "))
b = int(input("Ingresa el valor para b: "))
c = int(input("Ingresa el valor para c: "))
x1 = 0
x2 = 0

x1 = (-b + sqrt((b**2) - (4 * a * c))) / (2 * a)
x2 = (-b - sqrt((b**2) - (4 * a * c))) / (2 * a)

print("Valor para x1: " , x1)
print("Valor para x2: " , x2)
