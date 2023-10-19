"""Ejercicio 1

Escribe un programa que pida dos palabras y diga si riman o no. 
Si coinciden las tres últimas letras tiene que decir que riman. 
Si coinciden sólo las dos últimas tiene que decir que riman un poco y si no, que no riman."""


word1 = input("Ingresa una palabra")
word2 = input("Ingresa otra palabra")

word1_rima = word1[-3:]
word1_rima_poco = word1[-2:]

resultado_rima = word2.endswith(word1_rima)
resultado_rima_poco = word2.endswith(word1_rima_poco)

if resultado_rima:
    print("rima")
elif resultado_rima_poco:
    print("riman un poco")
else:
    print("No rima")