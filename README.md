# Number_Guessing_Game
# Overview
This is a number guessing game where the player has to guess a randomly generated sequence of 4 numbers. The numbers are between 0 and 3. After each guess, the game provides hints to help the player get closer to the correct sequence.

# Game Features:
* The player has 10 attempts to guess the correct sequence.
* The game generates a random sequence of 4 numbers, each between 0 and 3.
* After each guess, the game provides hints based on the player's input:
   *  "+" means that a number is correct and in the correct position.
   *  "-" means that a number is correct but in the wrong position.
   *  "*" means that a number is not in the sequence at all.
If the player guesses the correct sequence within 10 attempts, they win the game. If they do not guess correctly after 10 attempts, the game ends with a "Game Over" message.

# How to Play
1. When the game starts, the player is prompted to enter a guess for the sequence of 4 numbers.
2. The input should be a comma-separated list of 4 numbers, for example: 1, 2, 0, 3.
3. After each guess, the game provides hints to guide the player:
   *  A "+" indicates that a number is both correct and in the correct position.
   *  A "-" indicates that a number is correct but in the wrong position.
   *  A "*" indicates that a number is incorrect and does not appear in the sequence.
4. The player has a total of 10 attempts to guess the correct sequence.
5. If the player guesses correctly within the allowed attempts, they win the game. If not, the game ends with a "Game Over" message, and the correct sequence is revealed.
