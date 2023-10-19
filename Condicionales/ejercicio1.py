'''Ejercicio 1

Crear un programa que pida al usuario una letra, y si es vocal, muestre el mensaje "Es vocal". Si no, decirle al usuario que no es vocal'''

word = input("Ingresa una letra: ")

vocals = ["a", "e", "i", "o", "u"]

if word in vocals:
    print("Es vocal")
else:
    print("No es vocal")
