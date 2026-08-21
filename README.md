# Number Guessing Game

A terminal guessing game written in Python. The player chooses a number range and an attempt limit, then receives high/low hints until they guess the secret number or run out of attempts.

This began as a Day 2 Python learning project and was later extended with input validation, replay support, a game log, graceful exits, and a one-use cheat code.

---

## Features

- Choose the minimum and maximum values for the secret number.
- Choose how many guesses are allowed.
- Receive a high/low hint after each incorrect guess.
- Replay multiple rounds without restarting the script.
- Keep a log of wins, losses, and interrupted sessions.
- Use the hidden cheat-code flow once per round.
- Handle invalid input, `Ctrl+C`, and unavailable input cleanly.

---

## Requirements

- Python 3.x
- No third-party packages

The game uses Python's built-in `random` and `time` modules.

---

## Run It

Clone the repository and run the script:

```bash
git clone https://github.com/Innsaute-glitch/Guess-the-number-game.git
cd Guess-the-number-game
python Guess_the_number_game.py
```

You can also download `Guess_the_number_game.py` and run it directly.

---

## How To Play

1. Enter the minimum and maximum values for the range.
2. Enter a positive number of attempts.
3. Enter an integer guess when prompted.
4. Follow the high/low hints until you win or your attempts are exhausted.
5. Choose `y` to start another round or `n` to exit.

After repeated invalid replay responses, the script reveals an optional `s` command for changing or resetting the cheat code.

## Example

```text
>>> What is the minimum number you want? 1
>>> What is the maximum number you want? 10
>>> How many tries do you want? 3

--- Starting the guessing game... ---
>>> What is the number you are guessing? 7
Your guess was too low
>>> What is the number you are guessing? 9
Your guess was too high
```

## Project Structure

```text
Guess-the-number-game/
|-- Guess_the_number_game.py  # Game implementation
|-- README.md                 # Project documentation
|-- LICENSE                   # MIT license
```

## Learning Goals

This project practices functions, loops, conditionals, random number generation, exception handling, terminal input, mutable state, and formatted strings.

---

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
