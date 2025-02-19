# Simple Calculator

A desktop calculator application built with Python and PySide6, featuring a clean graphical user interface and robust arithmetic operations.

## Features

- Basic arithmetic operations (addition, subtraction, multiplication, division)
- Support for negative numbers
- Decimal number handling
- Error handling (e.g., division by zero)
- Number formatting for clean display
- Sequential operations support
- 10-digit number limit for display clarity

## Requirements

- Python 3.x
- PySide6

## Installation

1. Clone the repository
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the calculator using:
```bash
python -m src.main
```

## Testing

The project includes comprehensive unit tests for both calculator logic and GUI components. Run the tests using:
```bash
python -m unittest discover tests
```

## Project Structure

- `src/`
  - `calculator.py`: Core calculator logic
  - `gui.py`: GUI implementation using PySide6
  - `main.py`: Application entry point
- `tests/`
  - `test_calculator.py`: Calculator logic tests
  - `test_gui.py`: GUI component tests

## Features in Detail

- **Error Handling**: Graceful handling of division by zero and other errors
- **Number Formatting**: Automatic formatting of decimal numbers (removes trailing zeros)
- **State Management**: Maintains calculation state for sequential operations
- **Responsive GUI**: Clean interface with proper button sizing and layout
- **Input Validation**: Prevents numbers from becoming too large (10-digit limit)
