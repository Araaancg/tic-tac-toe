from random import choice
from math import inf

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