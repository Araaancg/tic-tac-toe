
class Player: # Clase jugador para guardar nombres y fichas
    def __init__(self, name) :
        self.name = name
        self.mark = None
    
    def setMark(self,letter):
        '''Asiganmos ficha al jugador, "X" o "O"'''
        self.mark = letter
    
    def __str__(self):
        return f"{self.name.capitalize()}: {self.mark}"

class Box: # Clase casilla (9 casillas en un tablero)
    def __init__(self,name,position):
        self.name = name
        self.position = position
        self.value = None
        self.isFull = False
    
    def fill(self,value):
        '''Asiganmos ficha a la casilla "X" o "O"'''
        self.value = value
        self.isFull = True if value else False

    def __str__(self):
        return f"Box: {self.position}"

class Board: # Clase tablero
    def __init__(self,array):
        self.array = array

    def empty(self):
        '''Vaciar tablero de fichas'''
        for box in self.array:
            box.fill(None)
    
    def emptyBoxes(self, **kwargs):
        '''Devuelve una lista de las casillas que están vacías'''
        if kwargs.get("full"): # por si necesitaba que me devolviera las casillas llenas en vez de las vacias
            return [box for box in self.array if box.isFull]
        return [box for box in self.array if not box.isFull]
    
    def pPrint(self, **kwargs):
        '''Imprime una representación visual del tablero'''
        boardDict = {}
        space = (kwargs.get("space")//2)-5 if kwargs.get("space") else 0
        for box in self.array:
            if kwargs.get("explanation") == box.name: # para la explicación
                boardDict[str(box.position)] = "X"
            else:
                boardDict[str(box.position)] = box.value if box.isFull else " " # si casilla vacía, asigna un espacio
        # el kwargs space es para centrar el tablero
        print(f'''
{' '.center(space)} {boardDict['(1, 1)']} | {boardDict['(1, 2)']} | {boardDict['(1, 3)']} 
{' '.center(space)}---|---|--- 
{' '.center(space)} {boardDict['(2, 1)']} | {boardDict['(2, 2)']} | {boardDict['(2, 3)']} 
{' '.center(space)}---|---|---
{' '.center(space)} {boardDict['(3, 1)']} | {boardDict['(3, 2)']} | {boardDict['(3, 3)']} 
''')
    
    def getWinner(self):
        '''Comprueba el estado del tablero
        - si hay ganador devuelve la ficha del ganador
        - si hay empate, devuelve la string "tie"
        - si la partida no ha terminado, devuelve None'''
        for symbol in ["X","O"]:
            allBoxes = [box for box in self.array if box.value == symbol]
            if len(allBoxes) >= 3: # mínimo 3 fichas de cada para ganar
                toWin = [] 
                # definir manualmente las diagonales porque las coordenadas no siguen patrón
                diag = [[(1,1),(2,2),(3,3)],[(1,3),(2,2),(3,1)]]
                toWin.append([box for box in allBoxes if box.position in diag[0]])
                toWin.append([box for box in allBoxes if box.position in diag[1]])

                for num in range(3):
                    toWin.append([box for box in allBoxes if box.position[0] == num+1]) # filas
                    toWin.append([box for box in allBoxes if box.position[1] == num+1]) # columnas
                # ToWin es una lista con 8 listas dentro, una por cada opción de victoria que hay
                for item in toWin:
                    if len(item) == 3: # si alguna sublista tiene 3 items, la línea está cubierta
                        return symbol
        if len(self.emptyBoxes()) == 0: # si nadie ha ganado, comprobar si hay empate
            return "tie"
        return None # partida no terminada
    
    def saveJson(self):
        '''Guardar la info del objeto tablero dentro de un diccionario para un archivo json'''
        boardDict = {}
        for box in self.array:
            boardDict[box.name] = box.value
        return boardDict 
        return {box.name:box.value for box in self.array} 

# Creamos un objeto BOX por cada casilla del tablero
box11 = Box("box11", (1,1))
box12 = Box("box12", (1,2))
box13 = Box("box13", (1,3))
box21 = Box("box21", (2,1))
box22 = Box("box22", (2,2))
box23 = Box("box22", (2,3))
box31 = Box("box31", (3,1))
box32 = Box("box32", (3,2))
box33 = Box("box33", (3,3))

# Creamos un objeto board que alberga todas las casillas del tablero (objetos Box)
board = Board([box11,box12,box13,box21,box22,box23,box31,box32,box33])