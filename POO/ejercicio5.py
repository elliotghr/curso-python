"""
Ejercicio 5

Crear un programa con tres clases Universidad, con atributos nombre (Donde se almacena el nombre de la Universidad). Otra llamada Carerra, con los atributos especialidad (En donde me guarda la especialidad de un estudiante). Una ultima llamada Estudiante, que tenga como atributos su nombre y edad. El programa debe imprimir la especialidad, edad, nombre y universidad de dicho estudiante con un objeto llamado persona.
"""


class Universidad:
    def universidad(self, universidad):
        self.universidad = universidad
        print(self.universidad)


class Carrera:
    def especialidad(self, especialidad):
        self.especialidad = especialidad
        print(self.especialidad)


class Estudiante(Universidad, Carrera):
    def setEstudiante(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        print(self.nombre)

persona = Estudiante()
persona.universidad("UNAM")
persona.especialidad("Sofware Developer")
persona.setEstudiante("Elliot", "27")
