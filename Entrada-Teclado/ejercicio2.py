"""
Ejercicio 2

Se desea tener un algoritmo que permita determinar y mostrar el promedio que ha obtenido un alumno en un determinado curso, conociendo las notas de: tres prácticas, el examen parcial y el examen final.

Considere:

PP = (P1 + P2 + P3) / 3
PROM = (PP + 2 * EP + 3 * EF) / 6


Donde: P1, P2, P3 : Practicas

PP: promedio de práctica

PROM: promedio

EP: examen parcial

EF: examen final
"""

print("Obtener el promedio de un alumno")
practica1 = float(input("Ingresa el valor para Practica 1: "))
practica2 = float(input("Ingresa el valor para Practica 2: "))
practica3 = float(input("Ingresa el valor para Practica 3: "))
examen_parcial = float(input("Ingresa el valor para examen parcial: "))
examen_final = float(input("Ingresa el valor para examen final: "))

promedio_practica = (practica1 + practica2 + practica3) / 3
promedio_final = (promedio_practica + 2 * examen_parcial + 3 * examen_final) / 6

print(promedio_final)
