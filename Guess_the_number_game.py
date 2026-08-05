# Import the required modules and define the necessary variables for clearing the console and cursor movement.
import random
import time

# Define the global variables to be used in the script
game_log = []
CURSOR_UP = '\033[1A'
CLEAR = '\x1b[2K'
CLEAR_LINE = CURSOR_UP + CLEAR
CODE = -1541

# Prompt the user for integer input and handle invalid inputs and KeyboardInterrupts
def get_integer_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("\t⚠️ This isn't a valid integer!")
        except KeyboardInterrupt:
            print()
            print("⚠️ A KeyboardInterrupt was detected!")
            game_log.append("Game_Interrupted")
            raise

# Define the function to get minimum and maximum numbers to be considered for solution by the user + set the solution
def get_solution():
    while True:
        min_num = get_integer_input(">>> What is the minimum number you want? ")
        max_num = get_integer_input(">>> What is the maximum number you want? ")
        if max_num < min_num:
            print("\t⚠️ Maximum number can not be less than Minimum number!")
        else:
            break
    solution = random.randint(min_num, max_num)
    time.sleep(0.2)
    print("--- The solution has been selected successfully!! ---\n\t   (Good luck for your attempts)")
    return solution

# Define the main function to run the game
def game():
    solution = get_solution()
    cheat_use = 0
    tries = 0
    while True:
        total_tries = get_integer_input(">>> How many tries do you want? ")
        if total_tries > 0:
            break
        elif total_tries == 0:
            print(CLEAR_LINE, end='')
            print(f"No.. wait! How can the game be started this way?!\nLemme check... number of tries is {total_tries}...\nAh man. Really now? 0 tries huh? (ᵕ—ᴗ—)\n")
        elif total_tries < 0:
            print(CLEAR_LINE, end='')
            print(f"No.. wait! How can the game be started in this way?!\nLemme check... number of tries is {total_tries}...Negative tries? For real? Atleast grace me with a 0 next time, I guess? (つ╥﹏╥)つ\n")
    print("\n--- Starting the guessing game... ---")
    while True:
        if tries < total_tries: # Run till all the tries are exhausted
            ans = get_integer_input(">>> What is the number you are guessing? ")
            if ans == solution:
                print("🎊 You guessed it successfully 🎊")
                time.sleep(0.2)
                print(f"CONGRATS! You cracked the code!! (Number of Tries taken: {tries + 1})")
                return "Game_Won"
            elif ans == CODE and cheat_use == False: # Allow the cheat code to be used anytime but only once here ig
                print("\n⋆⭒˚.⋆ ⟡ ݁₊ . Cheat code Activated!! ⟡ ݁₊ . ⋆⭒˚.⋆")
                time.sleep(0.4)
                print(f"The number is {solution}\n(Important: This will get erased in 2 seconds and cheat can not be used again!)") # Reveal the number
                cheat_use = True # Prevent reuse of cheat code
                time.sleep(2)
                print(CLEAR_LINE * 5, end='') # Clear cheat code message, number and evidence from the screen
            elif ans == CODE and cheat_use == True:
                print("⚠️ Cheat code has already been used!")
            elif ans > solution:
                tries += 1
                print(f"⬆️ Your guess was too high ⬆️ ({total_tries - tries}/{total_tries} more attempts remaining)")
            elif ans < solution:
                tries += 1
                print(f"⬇️ Your guess was too low ⬇️ ({total_tries - tries}/{total_tries} more attempts remaining)")
        else:
            time.sleep(0.2)
            print(f"\n💔 Attempts Exhausted... The answer was {solution}.")
            time.sleep(0.2)
            print("🔄 Better Luck Next Time 🔄")
            return "Game_Lost"

# Core of the script to run the game and handle KeyboardInterrupts and user input for replaying the game. Using all the defined functions and variables here!
try:
        game_log.append(game())
        start = False
except KeyboardInterrupt:
    print("Your game log was:", game_log)
    print("Exiting Successfully... Thanks for playing!")
while True:
    try:
        try_again = input("Do you want to try again? (y/n): ")
        if try_again.lower() == "y":
            game_log.append(game())
        elif try_again.lower() == "n":
            print("Your game log was:", game_log)
            print(f"--- Exiting the script successfully ... ---\n🙌 Thanks for playing 🙌")
            break
        else:
            print("\n⚠️ Invalid input! Please enter 'y' or 'n'.")
    except KeyboardInterrupt:
            print("Your game log was:", game_log)
            print("Exiting Successfully... Thanks for playing!")
            break
