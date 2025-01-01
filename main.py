# Importaciones
from funcs import * # archivo aparte de funciones
from classes import Player, board # archivo aparte de clases y objetos
from os import system # manejar terminal

user = ""

# '''
while user.lower() != "q": # q -> "quit", salir del programa
    system("clear")
    board.empty() # vacíamos tablero de fichas

    menuOptions = ["jugador vs jugador", "jugador vs IA1", "jugador vs IA2", "jugador vs IA3","explicación del juego","historial de partidas"]
    printMenu(mode="menú principal",array=menuOptions) # imprimimos el menú principal

    while True: # confirmar que el input es válido
        user = input("> ")
        if (user.isdigit() and int(user) in range(1,7)) or user.lower() == "q":
            break
        print("Input inválido, porfavor elija una de las opciones del menú con el número correspondiente\n")
    
    if user == "5": # explicación del juego
        system("clear")
        explainGame(board)
        system("clear")

    elif user == "6": # consultar historial
        system("clear")
        showLog(board) 
        input("Presiona enter para volver al menú principal ") 
        
    elif user.lower() != "q": # jugar h
        system("clear")
        players = getNames(mode=user, Player=Player)
        player1, player2 = players[0], players[1]
        system("clear")
        playGame(player1, player2, board, mode=user) 

# '''

