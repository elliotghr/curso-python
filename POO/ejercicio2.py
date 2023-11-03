"""
Ejercicio 2

Realizar un programa en el cual se declaren dos valores enteros por teclado utilizando el método __init__. Calcular después la suma, resta, multiplicación y división. Utilizar un método para cada una e imprimir los resultados obtenidos. Llamar a la clase Calculadora.
"""


class Calculadora:
    def __init__(self) -> None:
        self.valor1 = int(input("Please enter value 1: "))
        self.valor2 = int(input("Please enter value 2: "))

    def suma(self):
        resultado = self.valor1 + self.valor2
        print(resultado)

    def resta(self):
        resultado = self.valor1 - self.valor2
        print(resultado)

    def multiplicacion(self):
        resultado = self.valor1 * self.valor2
        print(resultado)

    def divison(self):
        resultado = self.valor1 / self.valor2
        print(resultado)

calculadora = Calculadora()
calculadora.suma()
calculadora.resta()
calculadora.multiplicacion()
calculadora.divison()
