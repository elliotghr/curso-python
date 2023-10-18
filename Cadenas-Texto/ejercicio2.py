'''
Ejercicio 2

Crear un programa que tenga una variable con la cadena “Separado” y un carácter de coma (,); e inserte el carácter entre cada letra de la cadena. Ej: separar y , debería devolver s,e,p,a,r,a,r

Pista: Debes utilizar un método de las cadenas llamado “Replace”, recuerda que la posición de los caracteres empieza en 0.
'''

phrase = "Separado"
phrase_replace = phrase.replace("", ",")
phrase_replace_strip = phrase_replace.strip(",")

print(phrase_replace_strip)