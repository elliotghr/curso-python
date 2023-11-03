"""
Ejercicio 3

Crear una clase Fabrica que tenga los atributos de Llantas, Color y Precio; luego crear dos clases mas que hereden de Fabrica, las cuales son Moto y Carro. Crear metodos que muestren la cantidad de llantas, color y precio de ambos transportes. Por ultimo, crear objetos para cada clase y mostrar por pantalla los atributos de cada uno
"""

class Fabrica:
    def __init__(self, llantas, color, precio):
        self.llantas = llantas
        self.color = color
        self.precio = precio

class Moto(Fabrica):
    def atributos(self):
        print(f"Llantas {self.llantas}")
        print(f"color {self.color}")
        print(f"precio {self.precio}")

class Carro(Fabrica):
    def atributos(self):
        print(f"Llantas {self.llantas}")
        print(f"color {self.color}")
        print(f"precio {self.precio}")

moto = Moto(2, "rojo", "12000")
moto.atributos()

carro = Carro(4, "azul", "220000")
carro.atributos()