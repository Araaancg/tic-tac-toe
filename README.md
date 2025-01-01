# Tic-Tac-Toe

## Overview

This is a terminal-based **Tic-Tac-Toe** game implemented in Python. The game allows a user to play tic-tac-toe in multiple modes, including playing against another player or against a computer with varying difficulty levels. 

The four modes are:
1. **Two-player mode**: Where two users can play against each other.
2. **AI Easy mode**: The AI makes random moves and is likely to lose if the user plays optimally.
3. **AI Medium mode**: The AI will try to avoid losing by blocking potential wins from the user, but it still makes random moves in non-critical situations.
4. **AI Hard mode**: The AI uses the **Minimax algorithm** to calculate the best possible move, guaranteeing either a win or a draw.

All games are logged in a JSON file (`logs.json`) for later reference. The logs can be viewed in the main menu.

---

## Languages and Technologies

- **Python**: The game is written in Python and runs in a terminal.
- **OOP (Object-Oriented Programming)**: The game utilizes object-oriented programming principles to manage the board, players, and game logic.
- **Minimax Algorithm**: Used in the AI to calculate optimal moves for the hardest difficulty.

Key Libraries and Files:
- **`ia.py`**: Defines three levels of AI players with different strategies.
- **`classes.py`**: Contains the classes that handle the board, users, and the game mechanics.
- **`funcs.py`**: Provides additional functions for the game.
- **`logs.json`**: Stores game logs, including moves made and results.

---

## Key Features

- Four game modes: 
  - **Two-player** mode
  - **Easy AI**
  - **Medium AI**
  - **Hard AI (Minimax)**
- Game logs are stored in `logs.json` and can be accessed during the game.
- Object-oriented design to manage game components (board, players, etc.).
- User-friendly terminal interface with simple navigation.
- Ability to consult past game logs through the main menu.

---

## Installation and Usage

### Prerequisites

- Python 3.x or later is required to run this project.

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/tic-tac-toe.git
   cd tic-tac-toe
   ```

2. (Optional) Create a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. No additional dependencies are needed since this project uses only built-in Python libraries.

### Running the Game

1. To start the game, run the executable file `main.py`:

   ```bash
   python main.py
   ```

2. The main menu will prompt you to select one of the four game modes. Use the arrow keys or the corresponding number to make your selection.
   
3. After the game finishes, your progress will be saved in `logs.json`. You can consult the logs during the game through the main menu.