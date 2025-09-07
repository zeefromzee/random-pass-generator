# Random Password Generator

A Python-based password generator that creates secure passwords with customizable **strength** and **memorability** options.

## Features

* Choose from **Weak**, **Medium**, or **Strong** password strength.
* Option to generate either:

  * **Memorable passwords** (easier to recall).
  * **Unmemorable passwords** (more secure, harder to guess).
* Automatically adjusts password length and character set based on your selection.

## Password Rules

* **Weak (6 characters)**

  * Memorable: lowercase letters + digits
  * Unmemorable: lowercase letters + digits + punctuation

* **Medium (8 characters)**

  * Memorable: uppercase + lowercase + digits
  * Unmemorable: uppercase + lowercase + digits + punctuation

* **Strong (12 characters)**

  * Memorable: uppercase + lowercase + digits + punctuation
  * Unmemorable: uppercase + lowercase + digits + punctuation (harder to memorize combinations)

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/random-password-generator.git
   cd random-password-generator
   ```
2. Run the script with Python:

   ```bash
   python3 random\ pass.py
   ```

## Usage

When you run the script, you’ll be prompted to:

1. Select password intensity (1 = Weak, 2 = Medium, 3 = Strong).
2. Choose memorability (a = memorable, b = unmemorable).

Example interaction:

```
Select password intensity (1-3):
1. Weak
2. Medium
3. Strong
2
a
Your medium memorable password is: Kd9rT7wQ
```

## Requirements

* Python 3.x

## Future Improvements

* Add option for custom password length.
* Add command-line arguments (no interactive prompts).
* Save generated passwords securely.

## License

This project is licensed under the MIT License – feel free to use and modify it.

