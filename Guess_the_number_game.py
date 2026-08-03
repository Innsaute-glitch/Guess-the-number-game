# This is the old version - Kept for memories!
# # Import the necessary modules
# import random
# import time

# # Generates a random number for the game to start
# print("""Random Number set successfully!!
# (The number is between 0 to 100)""")
# attempts = 10 # Set the variables
# cheat_use = 0
# inter = 0
# Starting = "y"
# CURSOR_UP = '\033[1A'
# CLEAR = '\x1b[2K'
# CLEAR_LINE = CURSOR_UP + CLEAR


# # Set up a loop
# def play(): # Put this as a function (Optimised after a few days)
#     number = random.randint(0,100)
#     # Wait a bit and print stuff along the way
#     time.sleep(0.5)
#     print("--- Starting the guessing game... ---")
#     time.sleep(0.5)
#     print("\nYou have 10 attempts to get it right... Best of luck!!!")
#     time.sleep(0.5)
#     attempts = 10 # Set the variables
#     cheat_use = 0
#     while inter == 0:
#         if attempts>0:
#             try: # Used a try command with some help
#                 guess = int(input("Guess the number: "))
#                 if guess>number:
#                     print("⬆️ Your guess was too high ⬆️")
#                     attempts -= 1
#                     print(f"Number of attempts remaining: {attempts}/10") # Use an f string
#                     time.sleep(0.5)
#                 elif guess<number:
#                     #Add a cheat code for fun and -1541 is always less than 0
#                     if cheat_use == 0 and attempts == 10 and guess == -1541:
#                         print()
#                         print("⋆⭒˚.⋆ ⟡ ݁₊ . Cheat code Activated!! ⟡ ݁₊ . ⋆⭒˚.⋆")
#                         time.sleep(0.5)
#                         print(f"The number is {number} (This will get erased in 2 seconds)") # Reveal the number
#                         cheat_use = 1
#                         time.sleep(2)
#                         print(CLEAR_LINE * 4, end='')
#                     else:
#                         print("⬇️ Your guess was too low ⬇️")
#                         attempts -= 1
#                         print(f"Number of attempts remaining: {attempts}/10") # Use an f string
#                         time.sleep(0.5)
#                 else:
#                     print()
#                     time.sleep(0.5)
#                     print("Wait.. You did it!")
#                     print("🎊 You guessed it successfully 🎊")
#                     time.sleep(1)
#                     tries = 10 - attempts + 1
#                     print()
#                     print(f"CONGRATS! You cracked the code!! (Total Tries: {tries})")
#                     print("🙌 Thanks for playing 🙌")
#                     break # Break the loop here
#             except ValueError:
#                 print("⚠️ This isn't a valid number... Please input an integer!")
#         else: # Check for the number of attempts
#             time.sleep(0.5)
#             print()
#             print("Attempts Exhausted... Better Luck Next Time 🔄")
#             print(f"The number was: {number}") # Print the number
#             print("🙌 Thanks for playing 🙌\n")
#             break # Break the loop (again)

# while True:
#     try:
#         if Starting == "y" and inter == 0:
#             play()
#             Starting = input("Play Again? (y/N): ").lower()
#         elif Starting == "n" and inter == 0:
#             print("Exiting the Script...\n")
#             break
#         else:
#             print("Please input either y or n...")
#             Starting = input("Play Again? (y/N): ").lower()
#     except KeyboardInterrupt: # Extra progress after a few days: Add keyboard interrupt to make it better
#             print("\nAlright mate - Exiting the script then")
#             print("🙌 Thanks for playing 🙌\n" \
#             "")
#             print()
#             inter = 1
#             break
#     except AttributeError:
#         print("Please input either y or n...")
# # The end :)

# This is the new upgraded version of the Guess the number game with more features and better code structure ig. The game now allows us to set a minimum and maximum number for guessing, and also handles invalid inputs and keyboard interrupts more gracefully ;)

# Import the required modules and define the necessary variables for clearing the console and cursor movement.
import random
import time
CURSOR_UP = '\033[1A'
CLEAR = '\x1b[2K'
CLEAR_LINE = CURSOR_UP + CLEAR

# Define the main function to take the user input and run the game
def get_play():
    while True:
        time.sleep(0.5)
        val = input(">>> What is the number you are guessing? ")
        try:
            val = int(val)
            return val
        except ValueError:
            print("\t⚠️ This isn't a valid integer!")

# Define the function to get minimum and maximum numbers to be considered for solution by the user + set the solution
def get_sol():
    while True:
        while True:
            try:
                min_num = int(input(">>> What is the minimum number you want? "))
                break
            except ValueError:
                print("\t⚠️ This isn't a valid integer!")
            except KeyboardInterrupt:
                print()
                print("⚠️ A KeyboardInterrupt was detected!")
                return "KeyInt" # KeyInt is used to exit the game if the user presses Ctrl+C
        while True:
            try:
                max_num = int(input(">>> What is the maximum number you want? "))
                break
            except ValueError:
                print("\t⚠️ This isn't a valid integer!")
            except KeyboardInterrupt:
                print()
                print("⚠️ A KeyboardInterrupt was detected!")
                return "KeyInt"
        if max_num < min_num:
            print("\t⚠️ Maximum number can not be less than Minimum number!")
        else:
            break
    sol = random.randint(min_num,max_num)
    time.sleep(0.5)
    print("--- The solution has been selected successfully!! ---\n\t   (Good luck for your attempts)")
    return(sol)

# Define the main function to run the game
def game():
    sol = get_sol()
    cheat_use = 0
    tries = 0
    if sol != "KeyInt": # No KeyInt detected. Else: Do Nothing
        while True: # Annoy the user till they give a valid integer for number of tries lmao
            try:
                tries_final = int(input("\nHow many tries do you want to have? "))
                break
            except ValueError:
                print("\t⚠️ Please input a valid integer!")
            except KeyboardInterrupt:
                print()
                print("⚠️ A KeyboardInterrupt was detected!")
                return "KeyInt"
        print("\n--- Starting the guessing game... ---")
    else:
        return "KeyInt"
    while sol != "KeyInt": # Run the game if KeyInt is not detected. Else: Do Nothing
        if tries < tries_final: # Run till all the tries are exhausted
            try:
                ans = get_play()
                if ans == sol:
                    print("🎊 You guessed it successfully 🎊")
                    time.sleep(0.5)
                    print(f"CONGRATS! You cracked the code!! (Number of Tries taken: {tries + 1})\n🙌")
                    return "Game_Won"
                elif ans == -1541 and cheat_use == 0 and ans != sol: # If cheat code is the answer itself, The answer will be revealed and the game will end, so no need to check for cheat code in that case. Code can be used anytime once.
                    print("\n⋆⭒˚.⋆ ⟡ ݁₊ . Cheat code Activated!! ⟡ ݁₊ . ⋆⭒˚.⋆")
                    time.sleep(0.5)
                    print(f"The number is {sol}\n(Important: This will get erased in 2 seconds and cheat can not be used again!)") # Reveal the number
                    cheat_use = 1 # Prevent reuse of cheat code
                    time.sleep(2)
                    print(CLEAR_LINE * 5, end='') # Clear cheat code message and number from the screen
                elif ans > sol:
                    tries += 1
                    print(f"⬆️ Your guess was too high ⬆️\n{tries_final - tries}/{tries_final} more attempts remaining.")
                elif ans < sol:
                    tries += 1
                    print(f"⬇️ Your guess was too low ⬇️\n{tries_final - tries}/{tries_final} more attempts remaining.")
            except KeyboardInterrupt:
                print("⚠️ A KeyboardInterrupt was detected!")
                return "KeyInt"
        elif tries_final == 0:
            print(CLEAR_LINE, end='')
            print(f"No.. wait! How can the game be started this way?!\nLemme check... number of tries is {tries_final}...\nAh man. Really now? 0 tries huh? (ᵕ—ᴗ—)\n")
            return "Invalid_Tries"
        elif tries_final < 0:
            print(CLEAR_LINE, end='')
            print(f"No.. wait! How can the game be started this way?!\nLemme check... number of tries is {tries_final}...Negative tries? For real? Atleast grace me with a 0 next time, I guess? (つ╥﹏╥)つ\n")
            return "Invalid_Tries"
        else:
            time.sleep(0.5)
            print(f"\n💔 Attempts Exhausted... The answer was {sol}.")
            time.sleep(0.5)
            print("🔄 Better Luck Next Time 🔄")
            return "Attempts_Exhausted"

games_played = 0 # Variable to keep track of the number of games played
# Now, start the main loop to run the game and ask the user if they want to play again. This utilizes all the above functions and is the main entry point of the script.

games_played += 1
KeyInt_check = game()
while KeyInt_check != "KeyInt": # Run the game till the user presses Ctrl+C. Else: Do Nothing
    if KeyInt_check == "Invalid_Tries":
        games_played -= 1 # Invalid tries should not be counted as a game played
    try:
        try_again = input("Do you want to try again? (y/n): ")
        if try_again.lower() == "y":
            games_played += 1
            KeyInt_check = game()
        elif try_again.lower() == "n":
            print(f"Number of games played: {games_played}\n--- Exiting the script successfully ... ---\n🙌 Thanks for playing 🙌")
            break
        else:
            print("\n⚠️ Invalid input! Please enter 'y' or 'n'.")
    except KeyboardInterrupt:
        print("⚠️ A KeyboardInterrupt was detected!")
        KeyInt_check = "KeyInt"
        break

if KeyInt_check == "KeyInt":
    print(f"\tNumber of games started: {games_played}\n\tSuccessful runs: {games_played - 1}\n--- The script was stopped successfully! ---\n🙌 Thanks for playing 🙌")
