import random
from hangman_art import stages
from hangman_wordlist import word_list

# Randomly choose a word from the word_list and assigns it to a variable called chosen_word, then prints
chosen_word = random.choice(word_list)

# Takes the chosen word and prints out a string of ---- to the same amount to signify the word
placeholder = ""
for letter in chosen_word:
    placeholder += "_"


game_over = False
correct_letters = []
wrong_letters = ""
lives = 6
print(placeholder)
print(stages[lives])

while not game_over:

    
    # Asks the user to guess a letter and assign it to a variable called user_guess. Make guess lowercase.
    user_guess = input("Guess a letter: ").lower()

    # Check if he letter the user guessed (user_guess) is within the generated word (chosen_word).
    # Replace the "-" in placeholder if the guessed letter is within the word.

    display = ""

    if (user_guess not in correct_letters):
        for letter in chosen_word:
            if (letter == user_guess):
                display += letter
                correct_letters.append(letter)
            elif (letter in correct_letters):
                display += letter
            else:
                display += "_"
    else:
        print("You have already guessed that letter.")
    
    if (user_guess not in correct_letters):
        lives -= 1
        print("\nYou guessed " + user_guess + ". That letter is not in the word. You now have " + str(lives) + "/6 left.")
        wrong_letters += user_guess + " "
        print("Incorrect letters you have guessed so far: " + wrong_letters)
        if (lives == 0):
            game_over = True
            print("Oh no, you lost!")
            print("\n\nThe word was " + chosen_word + ".")
    
    print(stages[lives])
    print("\n" + display)
    if(display == chosen_word):
        game_over = True
        print("\n\nThe word was " + chosen_word + ".")
        print("YOU WON!")

    
    