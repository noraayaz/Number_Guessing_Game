import random  

"""
Game Overview:
This is a number guessing game where the player has to guess a randomly generated sequence of 4 numbers.
The numbers are between 0 and 3. After each guess, the game provides hints:
    "+" means that a number is correct and in the correct position.
    "-" means that a number is correct but in the wrong position.
    "*" means that a number is not in the sequence.
The player has 10 attempts to guess the correct sequence. If they guess correctly, they win the game.
If they fail to guess within 10 attempts, the game ends with a "Game Over" message.
"""

# Get the user's guess input
def get_user_guess():
    # This loop keeps asking the user for input until they enter a valid guess.
    while True:
        # Ask the user to enter 4 numbers separated by commas.
        guess = input("Enter your 4 guesses (separate by comma, e.g., 0,1,2,3): ")
        
        try:
            # Split the user's input into a list of strings, then convert each to an integer.
            guess_list = [int(x) for x in guess.split(',')]
            
            # User entered exactly 4 numbers ?
            if len(guess_list) != 4:
                print("You need to enter exactly 4 numbers.")
                continue  # Go back to while loop.
            
            # All numbers are between 0 and 3 ?
            for number in guess_list:
                if number < 0 or number > 3:
                    print("All numbers must be between 0 and 3.")
                    break  # Exit the for-loop and go back to while loop.
            else:
                return guess_list
        
        except ValueError:
            print("Invalid input. Please enter valid numbers separated by commas (e.g., 0,1,2,3).")

# Give hints to user based on the user's guess
def give_hint(random_numbers, guess):
    hints = []  
    # This for loop will compare each number in the guess with the random number list.
    for i in range(4):
        if guess[i] == random_numbers[i]:
            hints.append("+")  # Number and position are correct, add "+".
        elif guess[i] in random_numbers:
            hints.append("-")  # Number is correct but in the wrong position, add "-".
        else:
            hints.append("*")  # Number is not in the list, add "*".
    return hints  

# Generate the random numbers
random_numbers = []
for i in range(4):  
    number = random.randint(0, 3)  # Generate a random number between 0 and 3.
    random_numbers.append(number)  # Add the random number to the list.
attempts = 0  # For tracking how many guesses the user has made.
max_attempts = 10  # A limit on the number of guesses.

print("\nWelcome to the Number Guessing Game!")
print("""\nGame Instructions:
To win the game, you need to guess a randomly generated sequence of 4 numbers.
The numbers will be between 0 and 3. After each guess, the game will provide you with hints:
1. "+" means that a number is correct and in the correct position.
2. "-" means that a number is correct but in the wrong position.
3. "*" means that a number is not in the sequence at all.
You have 10 attempts to guess the correct sequence. If you guess correctly, you win the game.
If you fail to guess the sequence within 10 attempts, the game will end with a "Game Over" message.
""")
print("\nTry to guess the 4-number sequence. The numbers are between 0 and 3.")


# This loop will allow the user to guess up to 10 times.
while attempts < max_attempts:
    guess = get_user_guess()  # Get the user's guess.
    attempts += 1  # Increase the attempt.

    if guess == random_numbers:  # Compare the lists.
        print(f"Congratulations! You've guessed the correct sequence in {attempts} attempts!")
        break  # Exit the loop.
    else:
        # Use the give_hint function to generate hints.
        hints = give_hint(random_numbers, guess)

        # hints is a list, like ['+', '-', '*', '+']
        hint_string = ' '.join(hints)  # Convert the hints list to a string with spaces.
        print("Hints: " + hint_string) 

        print(f"Attempt {attempts}/{max_attempts}")  # Print how many attempts are left.
        
    # If the maximum attempts are reached and the user hasn't guessed correctly:
    if attempts == max_attempts:
        print(f"Game over! The correct sequence was {random_numbers}. Better luck next time.")
        
    """ 'if attempts == max_attempts' inside the loop because: 
    After each guess, it needs to be controlled if the user has reached the maximum number of attempts.
    If the maximum attempts are reached, the game will immediately end with a "Game Over" message and 'while' loop will automatically stop
    because 'attempts' is no longer less than 'max_attempts'. """

"""
I benefited from ChatGPT in the following areas: 
ChatGPT suggested using the try-except block for handling user input errors
and writing the give_hint functionality as a separate function to improve the code's readability and maintainability.
ChatGPT also suggested using the join method to format the hints list as a string, making it more readable for the user.
I found these suggestions logical and implemented them in my code.
"""
