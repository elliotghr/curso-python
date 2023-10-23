"""Ejercicio 2

Con el siguiente diccionario, debes crear un programa que pregunte al usuario por un número; el programa debe imprimir el jugador al que hace referencia ese número

{
    1 : "Casillas", 
    15 : "Ramos",
    3 : "Pique", 
    5 : "Puyol",
    11 : "Capdevila", 
    14 : "Xabi Alonso",
    16 : "Busquets", 
    8 : "Xavi Hernandez",
    18 : "Pedrito", 
    6 : "Iniesta",
    7 : "Villa"
}
"""

players = {
    1: "Casillas",
    15: "Ramos",
    3: "Pique",
    5: "Puyol",
    11: "Capdevila",
    14: "Xabi Alonso",
    16: "Busquets",
    8: "Xavi Hernandez",
    18: "Pedrito",
    6: "Iniesta",
    7: "Villa",
}
try:
    player_num = int(input("Escribe el número de un juador de la selección Española: "))
    print(f"El jugador número {player_num} es: {players[player_num]}")
except Exception:
    print("Ese jugador no se encuentra")
