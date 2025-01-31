# Tkinter Calculator

## Description
This is a simple calculator built using Python's **Tkinter** library. It provides a graphical user interface (GUI) to perform basic arithmetic operations such as addition, subtraction, multiplication, and division.

## Features
- Supports basic arithmetic operations: `+`, `-`, `*`, `/`
- Parentheses support: `(` and `)`
- Clear button (`C`) to reset the calculation
- Error handling for invalid inputs
- Responsive and easy-to-use interface

## Installation
Ensure you have **Python** installed on your system (Python 3.12.2 recommended). You can check by running:

```sh
python --version
```

If Python is installed, the Tkinter library is usually included by default. If not, install it using:

```sh
pip install tk
```

## Usage
1. Clone the repository (or download the script):

```sh
https://github.com/manashbaral/tkinter-calculator.git
```

2. Run the Python script:

```sh
python calculator.py
```

3. Use the buttons to enter a mathematical expression and press `=` to compute the result.

## Code Overview
The script consists of:
- **Global variable `calculation`**: Stores the current input.
- **Functions**:
  - `add_to_calculation(symbol)`: Appends a number/operator to the input.
  - `evaluate_calc()`: Evaluates the expression and displays the result.
  - `clear_field()`: Clears the input field.
- **Tkinter GUI components**: Buttons for digits (0-9), operators, and control actions.

## Screenshot
![Calculator Screenshot](https://via.placeholder.com/400x300?text=Calculator+Screenshot)

## Future Improvements
- Implement keyboard support for input.
- Enhance UI with better styling.
- Add support for advanced mathematical functions.

## Contributing
Feel free to fork this repository, make changes, and submit a pull request!

## License
This project is open-source and available under the [MIT License](LICENSE).

## Author
Manash Baral



