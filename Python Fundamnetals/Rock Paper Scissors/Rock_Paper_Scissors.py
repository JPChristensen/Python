import random

play_again = True
while play_again:
    users_choice = input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors. If you would like to quit, press 9. \nChoice: ")
    try:
        users_choice = int(users_choice)
        if (users_choice == 9):
            print("Quitting Game.")
            play_again = False
        elif(users_choice < 0 or users_choice > 2):
            print("Invalid choice. Try Again.")
        else:
            computer_choice = random.randint(0,2)
            choices = ["Rock","Paper","Scissors"]

            print(f"You chose {choices[users_choice]}")
            print(f"Computer chose {choices[computer_choice]}")

            # 0 for Rock
            # 1 for Paper
            # 2 for Scissors

            if (users_choice == computer_choice):
                print("You draw!")
            elif (users_choice == 0): # User chose Rock
                if (computer_choice == 2): # Computer chose Scissors
                    print("You Win!")
                else:
                    print("You Lose!")
            elif (users_choice == 1): # User chose Paper
                if (computer_choice == 0): # Computer chose Rock
                    print("You Win!")
                else:
                    print("You Lose") # Computer chose Scissors
            elif (users_choice == 2): # User chose Scissors
                if (computer_choice == 1): # Computer chose paper.
                    print("You Win!")
                else:
                    print("You Lose!") # Computer chose rock.
    except:
        print("No number entered. Try Again.")


    