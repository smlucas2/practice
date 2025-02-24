# Hot Cold Game

An interactive number guessing game where players try to guess a randomly generated number between 1 and 100.

## Installation

1. Clone the repository
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

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
