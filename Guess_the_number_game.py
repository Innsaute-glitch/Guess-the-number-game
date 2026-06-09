# Import the necessary modules
import random
import time 

# Generates a random number for the game to start
print("""Random Number set successfully!!
(The number is between 0 to 100)""")
attempts = 10 # Set the variables
cheat_use = 0
inter = 0


# Set up a loop
def play(): # Put this as a function (Optimised after a few days)
    number = random.randint(0,100)
    # Wait a bit and print stuff along the way
    time.sleep(0.5)
    print("--- Starting the guessing game... ---")
    time.sleep(0.5)
    print("\nYou have 10 attempts to get it right... Best of luck!!!")
    time.sleep(0.5)
    attempts = 10 # Set the variables
    cheat_use = 0
    while inter == 0:
        if attempts>0:
            try: # Used a try command with some help
                guess = int(input("Guess the number: "))
                if guess>number:
                    print("⬆️ Your guess was too high ⬆️")
                    attempts -= 1
                    print(f"Number of attempts remaining: {attempts}/10") # Use an f string
                    time.sleep(0.5)
                elif guess<number:
                    #Add a cheat code for fun and -1541 is always less than 0
                    if cheat_use == 0 and attempts == 10 and guess == -1541:
                        print()
                        print("⋆⭒˚.⋆ ⟡ ݁₊ . Cheat code Activated!! ⟡ ݁₊ . ⋆⭒˚.⋆")
                        time.sleep(0.5)
                        print(f"The number is {number}") # Reveal the number
                        cheat_use = 1
                        print()
                    else:
                        print("⬇️ Your guess was too low ⬇️")
                        attempts -= 1
                        print(f"Number of attempts remaining: {attempts}/10") # Use an f string
                        time.sleep(0.5)
                else:
                    print()
                    time.sleep(0.5)
                    print("Wait.. You did it!")
                    print("🎊 You guessed it successfully 🎊")
                    time.sleep(1)
                    tries = 10 - attempts + 1
                    print()
                    print(f"CONGRATS! You cracked the code!! (Total Tries: {tries})")
                    print("🙌 Thanks for playing 🙌")
                    break # Break the loop here
            except ValueError:
                print("⚠️ This isn't a valid number... Please input an integer!")
        else: # Check for the number of attempts
            time.sleep(0.5)
            print()
            print("Attempts Exhausted... Better Luck Next Time 🔄")
            print(f"The number was: {number}") # Print the number
            print("🙌 Thanks for playing 🙌\n")
            break # Break the loop (again)

Starting = "y"
while True:
    try:
        if Starting == "y" and inter == 0:
            play()
            Starting = input("Play Again? (y/N): ").lower()
        elif Starting == "n" and inter == 0:
            print("Exiting the Script...\n")
            break
        else:
            print("Please input either y or n...")
            Starting = input("Play Again? (y/N): ").lower()
    except KeyboardInterrupt: # Extra progress after a few days: Add keyboard interrupt to make it better
            print("\nAlright mate - Exiting the script then")
            print("🙌 Thanks for playing 🙌\n" \
            "")
            print()
            inter = 1
            break
    except AttributeError:
        print("Please input either y or n...")
# The end :)