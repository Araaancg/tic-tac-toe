# Tic-Tac-Toe

## Descripción

Este es un juego de **Tic-Tac-Toe** basado en terminal, implementado en Python. El juego permite al usuario jugar en varios modos, incluyendo jugar contra otro jugador o contra una computadora con diferentes niveles de dificultad.

Los cuatro modos son:
1. **Modo dos jugadores**: Donde dos usuarios pueden jugar entre sí.
2. **Modo IA fácil**: La IA hace movimientos aleatorios y probablemente perderá si el usuario juega de manera óptima.
3. **Modo IA media**: La IA intentará no perder, bloqueando las posibles victorias del usuario, pero todavía hace movimientos aleatorios en situaciones no críticas.
4. **Modo IA difícil**: La IA utiliza el algoritmo **Minimax** para calcular el mejor movimiento posible, garantizando una victoria o empate.

Todos los juegos se registran en un archivo JSON (`logs.json`) para su referencia posterior. Los registros pueden ser consultados en el menú principal.

---

## Lenguajes y Tecnologías

- **Python**: El juego está escrito en Python y se ejecuta en una terminal.
- **OOP (Programación Orientada a Objetos)**: El juego utiliza principios de programación orientada a objetos para gestionar el tablero, los jugadores y la lógica del juego.
- **Algoritmo Minimax**: Utilizado en la IA para calcular los movimientos óptimos en la dificultad más alta.

Librerías y Archivos Claves:
- **`ia.py`**: Define tres niveles de jugadores IA con diferentes estrategias.
- **`classes.py`**: Contiene las clases que gestionan el tablero, los jugadores y la mecánica del juego.
- **`funcs.py`**: Proporciona funciones adicionales para el juego.
- **`logs.json`**: Almacena los registros de los juegos, incluyendo los movimientos realizados y los resultados.

---

## Características Principales

- Cuatro modos de juego:
  - **Modo dos jugadores**
  - **IA fácil**
  - **IA media**
  - **IA difícil (Minimax)**
- Los registros de los juegos se almacenan en `logs.json` y se pueden consultar durante el juego.
- Diseño orientado a objetos para gestionar los componentes del juego (tablero, jugadores, etc.).
- Interfaz de terminal fácil de usar con navegación simple.
- Opción para consultar los registros de juegos pasados a través del menú principal.

---

## Instalación y Uso

### Requisitos Previos

- Python 3.x o superior es necesario para ejecutar este proyecto.

### Instalación

1. Clona el repositorio:

   ```bash
   git clone https://github.com/tuusuario/tic-tac-toe.git
   cd tic-tac-toe
   ```

2. (Opcional) Crea un entorno virtual:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # En Windows, usa `venv\Scripts\activate`
   ```

3. No se requieren dependencias adicionales, ya que este proyecto solo utiliza bibliotecas integradas de Python.

---

### Ejecutar el Juego

1. Para comenzar el juego, ejecuta el archivo `main.py`:

   ```bash
   python main.py
   ```

2. El menú principal te pedirá seleccionar uno de los cuatro modos de juego. Usa las teclas de dirección o el número correspondiente para hacer tu selección.
   
3. Después de que termine el juego, tu progreso se guardará en `logs.json`. Puedes consultar los registros durante el juego a través del menú principal.