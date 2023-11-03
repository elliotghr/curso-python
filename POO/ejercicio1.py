"""
Ejercicio 1

Realizar un programa que conste de una clase llamada Estudiante, que tenga como atributos el nombre y la nota del alumno. Definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.
"""

class Estudiante:
    def __init__(self, nombre, nota):
        self._nombre = nombre
        self._nota = nota

    def getNombre(self):
        print(self._nombre)
    
    def getNota(self):
        print(self._nota)
    
    def resultado(self):
        if (self._nota < 6):
            print("Reprobado")
        else:
            print("Aprobado")
        

estudiante1 = Estudiante("Juan", 5)
estudiante1.getNombre()
estudiante1.getNota()
estudiante1.resultado()