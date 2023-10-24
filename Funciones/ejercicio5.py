"""
Ejercicio 5

Crear un programa que tenga dos funciones, una que contenga el area de un cuadrado con argumento de lado; y la otra el area de un circulo con argumento de radio

"""
import math


def area_cuadrado(lado):
    area = lado * lado
    return area


def area_circulo(radio):
    area = math.pi * math.pow(radio, 2)
    return area


cuadrado = area_cuadrado(5)
circulo = area_circulo(5)

print(cuadrado, circulo)
