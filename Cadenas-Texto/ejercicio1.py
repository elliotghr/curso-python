'''
Ejercicio 1

Crear un programa, que tenga una variable con la cadena “Te quiero solo como amigo”, y muestre la siguiente información:

• Imprima los dos primeros caracteres.

• Imprima los tres últimos caracteres.

• Imprima dicha cadena cada dos caracteres. Ej.: Si la cadena fuera “recta” debería imprimir rca

• Dicha cadena en sentido inverso. Ej.: Si la cadena fuera hola mundo! debe imprimir !odnum aloh

• Imprima la cadena en un sentido y en sentido inverso. Ej: Si la cadena es “reflejo” imprime reflejoojelfer.
'''
phrase = "Te quiero solo como amigo"

print(phrase[0:2])
print(phrase[-3:])
print(phrase[0:2])
print(phrase[0::2])
print(phrase[::-1])
print(phrase, phrase[::-1])
