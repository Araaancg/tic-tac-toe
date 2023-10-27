from os import system # manejo de terminal
from random import randint, choice
from math import inf # para la función minimax
import datetime as dt # para la fecha del historial de partidas
import json # para guardar el historial

# IAS
def ai1(board):
    '''Elige aleatoriamente entre las casilals que están vacías'''
    return choice(board.emptyBoxes()) 

def ai2(board, userPlayer):
    '''Devuelve casilla que le da la victoria al usuario en el caso de que se dé
    sino devuelve una casilla random de las que estén vacías'''
    for box in board.emptyBoxes(): # iterar por las casillas vacías
        box.fill(userPlayer) # rellenar la casilla con la ficha del usuario
        if board.getWinner() == userPlayer: # comprobar si gana
            return box # si lo hace devolver esa casilla
        box.fill(None) # si no, vaciar casilla y continuar iterando
    return ai1(board) # si el bucle termina sin activar el return, devolver una casilla aleatoriamente

def ai3(board, aiPlayer, userPlayer):
    '''Utilizando la función minimax, esta función devuelve la casilla que tiene más
    probabilidades de dar la victoria a la ia'''
    bestScore = -inf
    bestMove = None
    for box in board.emptyBoxes():
        box.fill(aiPlayer)
        score = minimax(board, False, aiPlayer, userPlayer)
        box.fill(None)
        if (score > bestScore):
            bestScore = score
            bestMove = box
    return bestMove

def minimax(board, isMaxTurn, maximizerMark, minimizerMark): 
    # Comprobar estado del tablero, devolver 1 si gana ia, -1 si pierde y 0 si es empate
    if board.getWinner() == maximizerMark:
        return 1
    elif board.getWinner() == minimizerMark:
        return -1
    elif board.getWinner() == "tie":
        return 0
    else: # Si la partida no ha terminado continuar analizando posibles ramas
        turn = minimizerMark
        bestScore = inf
        if isMaxTurn:
            turn = maximizerMark
            bestScore = -inf

        for box in board.emptyBoxes():
            box.fill(turn)
            score = minimax(board, not isMaxTurn, maximizerMark, minimizerMark)
            box.fill(None)
            bestScore = max(score, bestScore) if isMaxTurn else min(score, bestScore)

        return bestScore

# OTRAS FUNCIONES
def printMenu(mode,array): 
    ''' Imprimir un menú apartir de una lista de opciones'''
    print(" ")
    print(mode.upper().center(15), "\n")
    for i, option in enumerate(array):
        print(f"{i+1}. {option}")
    print("Q. salir")
    print(" ")

def checkInput(userIn, board):
    '''Confirma que el input que ha dado el usuario para poner una ficha en el tablero es correcto'''
    try:
        userIn = (int(userIn.split(',')[0]),int(userIn.split(',')[1]))
    except:
        return {"input":False,"msg":"Formato incorrecto. El input deben ser dos ints separados por una coma. ej: 1,2"}
    else:
        if 1 <= userIn[0] < 4 and 1 <= userIn[1] < 4:
            for boxObject in board.array:
                if boxObject.position == userIn:
                    box = boxObject
                    break
            if not box.isFull:
                return {"input":True,"box":box}
            return {"input":False,"msg":"Por favor, elija una casilla vacía"}
        return {"input":False,"msg":"Números fuera de rango, deben de ir del 1 al 3, ambos incluidos"}

def getNames(mode, Player):
    '''Pregunta por los nombre(s) de usuario(s) y crea objeto(s) Player'''
    player1, player2 = None, None
    ias = ["IA1", "IA2", "IA3"]
    while True:
        name1 = input("Jugador 1, introduce tu nombre: ")
        name2 = ias[int(mode)-2]
        if mode == "1":
            name2 = input("Jugador 2, introduce tu nombre: ")

        if name1 != name2:
            player1 = Player(name=name1)
            player2 = Player(name=name2)
            break
        print("Los nombres no pueden ser iguales. En los modos de juego 2, 3 y 4, los nombres: 'IA1', 'IA2' e 'IA3' son nombres reservados")
    return player1,player2

def getData(jsonFile): 
    '''Coge el nombre de un archivo json y te devuelve el contenido 
    del archivo en un diccionario'''
    with open(jsonFile,encoding="utf8") as file:
        return json.load(file)

def saveGame(board,player1,player2,gameMode):
    '''Coge la info del archivo .json en un diccionario, actualiza el diccionario con la nueva partida
    y vuelve a guardar el diccionario en el archivo .json'''
    log = getData("log.json")
    provDicc = {
        "date":dt.datetime.isoformat(dt.datetime.now()).split("T")[0], # solo guardamos a año, mes y día
        "finalBoard":board.saveJson(),
        "gameMode":gameMode,
        "players": [
            {"name":player1.name,"mark":player1.mark},
            {"name":player2.name,"mark":player2.mark}
        ],
        "winner":board.getWinner() if board.getWinner != "tie" else None
    }
    log["log"].append(provDicc)
    with open("./log.json", mode="w", encoding="utf8") as file:
        json.dump(log,file,ensure_ascii=False,indent=4)

def playGame(player1, player2, board, mode):
    '''
    Desarrolla el juego de tres en raya completo. Requiere:
    - dos objetos player, ya sean dos usuarios o una ia y un usuario
    - int que indique el modo de juego:
            1 = jugador vs jugador
            2 = jugador vs ia tonta
            3 = jugador vs ia que tapa cuando vas a ganar
            4 = jugador vs ia que no pierde
    - un objeto Board (tablero) vacío
    '''
    gameDone = False 
    count = randint(1,2) # determinar quien empieza
    box = None 
    turn = ""

    # el jugador que empiza se le asigna la ficha 'X'
    isTurnPly1 = True if count == 1 else False
    marks = ["X","O"]
    if not isTurnPly1:
        marks.reverse()
    player1.setMark(marks[0]) 
    player2.setMark(marks[1]) 

    while not gameDone: # el bucle termina cuando se termine la partida
        system("clear")
        board.pPrint() # mostramos estado del tablero

        if box and mode != "1": # si se juega en los modos 2,3 o 4 mostramos la jugada de la ia
            print(f"{player2.name} choose {box.position}")

        turn = player1 if isTurnPly1 else player2 # asignamos a la variable 'turn' el objeto jugador que toque
        print(f"\nTurno de {turn.name.upper()} - {turn.mark}")
        print("Introduce las coordenadas de la casilla deseada (fila,columna)\n")

        # PONEMOS FICHA EN EL TABLERO
        # Modo 1: jugador vs jugador
        if mode == "1" or turn.name not in ["IA1","IA2","IA3"]: # siempre que sea turno de un usuario
            invalidInput = True
            while invalidInput: # Confirmamos que el input es válido
                userChoice = input("> ")
                isValid = checkInput(userChoice, board) 
                if isValid["input"]:
                    invalidInput = False
                    box = isValid["box"]
                else:
                    print(isValid["msg"]) # Imprimimos mensaje de error
        # Modo 2: jugador vs ia1 (pone la ficha aleatoriamente) 
        if mode == "2" and turn.name == "IA1":
            box = ai1(board) 
        # Modo 3: jugador vs ia2 (tapa cuando vas a ganar)
        if mode == "3" and turn.name == "IA2":
            box = ai2(board, player1.mark)
        # Modo 4: jugador vs ia3 (va a ganar o como poco a empatar)
        if mode == "4" and turn.name == "IA3":
            box = ai3(board, player2.mark, player1.mark)
    
        box.fill(turn.mark) # ponemos la ficha del jugador en la casilla elegida

        # COMPROBAMOS ESTADO DEL TABLERO
        if board.getWinner():
            system("clear")
            board.pPrint()
            saveGame(board,player1,player2,mode)
            if board.getWinner() == turn.mark:
                print("¡"+turn.name.upper()+" HA GANADO!")
            else:
                print("¡EMPATE!")
            input("\nPresiona enter para volver al menú principal ")
            gameDone = True # se temrina el bucle

        isTurnPly1 = not isTurnPly1 # cambiamos de turno

def showLog(board): 
    '''Mostramos el registro de partidas'''
    log = getData("log.json")["log"]
    for i,game in enumerate(log):
        print(" ")
        vsString = f"{game['players'][0]['mark']} - {game['players'][0]['name'].upper()} VS {game['players'][1]['name'].upper()} - {game['players'][1 ]['mark']}"
        print(vsString)
        print(game["date"].center(len(vsString)))
        # manipulamos objeto board con info del historial de partida
        for k,v in game["finalBoard"].items():
            for box in board.array:
                if box.name == k:
                    box.fill(v)
        board.pPrint(space=len(vsString))
        if i != len(log)-1:
            print("----------".center(len(vsString)))
        
def explainGame(board):
    print(f'''
Este es el famoso juego de tres en raya. En el menú prinicpal podrás elegir entre los diferentes modos
de juego. El programa en sí cuenta con 4 modos.
    - Modo 1: jugador vs jugador, perfecto para jugar contra un amigo
    - Modo 2: usuario vs ia1, jugar contra una máquina, muy mal lo tienes que hacer para perder
    - Modo 3: usuario vs ia2, esta de aquí intenta a toda costa no perder, el empate es su especialidad
    - Modo 4: usuario vs ia3, una máquina que nunca pierde, puedes considerar que el empate contra esta
    ia es una victoria

Una vez elijas el modo de juego tendrás que introducir tú nombre, en caso de dos jugadores se te pedirán
dos nombres. A tener en cuenta que los nombres no pueden ser iguales, igual pasa si se juega contra la máquina,
los nombres "IA1", "IA2" e "IA3" son reservados.

Cuando empiece el juego se te mostrará un tablero como este''')
    board.pPrint()
    print('''
El jugador que empiece será aleatorio y siempre se le asignará la ficha "X". Para poner una ficha
en el tablero se deberán indicar las coordenadas de la casilla deseada, indicando con números del 1 al 3
la fila y la columna separados por una coma.
Aquí abajo vemos un ejemplo de la ficha "X" en la casilla 1,2 (fila 1, columna 2)''')
    board.pPrint(explanation="box12")
    print('''
Por último decir que en el menú principal se te presentarán dos opciones más, en la opción 6 se podrá consultar
el historial de partidas y en la opción "Q" se podrá finalizar le programa.
''')
    input("Presiona enter para volver al menú principal ")