import random

logo = """
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ' _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|     
"""

def easy(Number_to_guess):
    guesses = 10
    continue_game = True
    
    while continue_game:
        print(f"You have {guesses} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        if(Number_to_guess == guess):
            print("You have guesses the correct number! You Win!")
            continue_game = False
        elif (Number_to_guess < guess):
            print("Too High.")
            guesses -= 1
        else:
            print("Too Low.")
            guesses -= 1
        
        if (guesses == 0):
            continue_game = False
            print("You have 0 remaining guess. You lose.")



def hard(Number_to_guess):
    guesses = 5
    continue_game = True
    
    while continue_game:
        print(f"You have {guesses} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        if(Number_to_guess == guess):
            print("You have guesses the correct number! You Win!")
            continue_game = False
        elif (Number_to_guess < guess):
            print("Too High.")
            guesses -= 1
        else:
            print("Too Low.")
            guesses -= 1
        
        if (guesses == 0):
            continue_game = False
            print("You have 0 remaining guess. You lose.")



def main():
    Number_to_guess = int(random.randrange(0,101))
    print(Number_to_guess)
    print(logo + "\n")
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficult. Type 'easy' or 'hard':  ")

    if(difficulty == 'easy'):
        easy(Number_to_guess)
    elif (difficulty == 'hard'):
        hard(Number_to_guess)
    else:
        print("Invalid Option.")



main()