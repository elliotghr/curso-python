'''Ejercicio 1

En la siguiente lista, debes hacer un programa que muestre los valores al usuario, a su vez, debe pedir dos datos y esos que sean ingresados deben ser sustituidos en el primer y segundo lugar:

[20, 50, "Curso", 'Python', 3.14]
'''

lista = [20, 50, "Curso", 'Python', 3.14]
lista_str = [str(elemento) for elemento in lista]
values = (", ".join(lista_str))

print(f"Tiene disponible los siguientes valores: {values}")
first_value = input("Escribe un valor para cambiar la primera posición: ")
last_value = input("Escribe otro valor para cambiar la segunda posición: ")


lista_str[0] = first_value
lista_str[1] = last_value
values = (", ".join(lista_str))

print(values)