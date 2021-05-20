from random import randint
from art import logo

def game():
    #Add Logo
    print(logo + "\n")

    #Start game
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    #Get a random number
    number = randint(1,100)
    #Set difficulty and get number of attempts
    attempts = set_difficulty()
    #Start playing with the selected
    play(attempts,number)

def set_difficulty():
    #Ask for difficulty
    difficulty = {
        "easy": 10,
        "hard": 5
    }

    difficulty_choose = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    return difficulty[difficulty_choose]

def play(attempts,number):
    
    print(f"You have {attempts} remaining to guess the number")
    guess = int(input("Make a guess: "))

    attempts = validate_guess(guess,number,attempts)

    if attempts == 0:
        print(f"You've run out of guesses, you lose.")
    elif guess != number:
        print("Guess again.")
        play(attempts,number)
    

def validate_guess(guess,number,attempts):
    if guess > number:
        print("Too high")
        return attempts - 1
    elif guess < number:
        print("Too low")
        return attempts - 1 
    else:
        print (f"You got it! The answer was {number}.")
        return attempts

game()