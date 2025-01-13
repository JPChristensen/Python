# Treasure Island
import time

print("Welcome to Treasure Island!")
keep_playing = True

while(keep_playing):

    path = str(input("On your way to the treasure you come to a crossroads, which do you choose? Left or Right?\n"))

    if (path == "left" or path == "Left"):
        print("You continue on your path.\n\n")
        time.sleep(2)

        boat = str(input("At the end of the path, you come across a lake. You can see that a boat is heading your way but very slowly, you estimate it will be around 2 hours. \nYou have also determined that swimming across is very possible. \nDo you choose to wait or swim?\n"))

        if (boat == "wait" or boat == "Wait"):
            print("You wait for the boat and it carries you across safely.\n\n")
            time.sleep(2)

            door = str(input("At the otherside of the lake, you see a tunnel, you decide to travel into the tunnel which leads to three doors, a red door, a blue door, or a yellow door. Which door do you choose to take?\n"))

            if (door == "blue" or door == "Blue"):
                print("You found the treasure!")
            else:
                print("So close. Game Over.")
        else:
                print("Game Over.")
    else:
        print("Game Over.")

    play_again = input("Would you like to play again? Y or N?")
    if (play_again == "Y" or play_again == "y"):
         keep_playing = True
    else:
         keep_playing = False