# Hot Cold Game

An interactive number guessing game built with Python and PySide6 where players try to guess a randomly generated number between 1 and 100. The game provides immediate visual feedback ("hot" if closer, "cold" if farther) during the guessing process.

## Features

- Random number generation between 1 and 100
- Modern PySide6-based GUI with:
  - Multi-function start/feedback button
  - Input field for guesses
- Dynamic hot/cold feedback system
- Automatic game reset after winning

## Requirements

- Python 3.6+
- PySide6

## Installation

1. Install the required dependencies:
```bash
pip install PySide6
```

2. Clone or download this repository

## Running the Game

From the project root directory:

```bash
python src/main.py
```

## How to Play

1. Click the "Start Game" button to begin
2. Enter a number between 1 and 100 in the input field
3. Press Enter or click the button to submit your guess
4. The feedback button will show:
   - "hot" (red) if you're getting closer
   - "cold" (blue) if you're getting farther
   - "WINNER!" (green) if you guess correctly
5. After winning, the game will automatically reset after 2 seconds

## Running Tests

From the project root directory:

```bash
python -m unittest tests/test_game_logic.py
```

## Project Structure

```
hot_cold/
├── README.md
├── src/
│   ├── main.py           # Application entry point
│   ├── game_logic.py     # Core game mechanics
│   └── gui.py            # PySide6 interface
└── tests/
    └── test_game_logic.py # Unit tests
```

## Architecture

The project follows a modular design with clear separation between game logic and UI components:

- `game_logic.py`: Handles core gameplay mechanics including random number generation, guess validation, and feedback calculation
- `gui.py`: Manages the graphical interface using PySide6, including the start/feedback button and input field
- `main.py`: Application entry point that initializes the GUI and starts the event loop
