import random
import cards

game_on = True
logo = '''.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _' |/ __| |/ / |/ _' |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
'-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\

      |  \/ K|                            _/ |                
      '------'                           |__/'''

# Function to deal the user's and computer hand.
def deal_card():
    card = ""
    # Deal hands
    card = (random.choice(cards.ranks))

    return card

# Convnerts the face rank to an integer and returns the value.
def convert_card_rank_to_num(card):
    value = 0
    if (card in ["J","Q","K"]):
        value = 10
    elif (card == "A"):
        value = 11
    else:
        value = int(card)

    return value

# returns final score
def calculate_score(cards):
    total = 0
    for card in cards:
        total += convert_card_rank_to_num(card)
    
    # "A" counts as 11 until the total score is over 21, then it will count as 1 to avoid bust.
    if ("A" in cards and total > 21):
            total -= 10
    return total

# Determines the winner
def calculate_winner(players_hand, computers_hand):
        players_total = calculate_score(players_hand)
        computers_total = calculate_score(computers_hand)

        winner = ""
        print(f"Your cards are {players_hand}, with final score: {players_total}")
        print(f"Computers cards are {computers_hand}, with final score: {computers_total}")
        if (players_total > 21):
            winner = "You Lose!"
        elif (computers_total > 21):
            winner = "You Win!"
        elif (players_total == computers_total):
            winner = "Draw!"
        elif (players_total > computers_total):
            winner = "You Win!"
        else:
            winner = "You Lose!"

        print(winner + "\n\n\n\n\n")

# Game Board
while game_on:
    # Confirm the player wants to play a game
    game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

    # if the player says no, exit game board, else Game on.
    if (game == 'n'):
        game_on = False
    else:
        print(logo)

        # Deals the players hand
        players_hand = [] 
        players_hand.append(deal_card())
        players_hand.append(deal_card())

        # Deals the computers hand
        computers_hand = []
        computers_hand.append(deal_card())
        computers_hand.append(deal_card())

        # Prompt user if they want another card, if it exceeds 21, automatically lose.
        another_card = True
        while another_card:
            print(f"Your cards are {players_hand}, with current score: {calculate_score(players_hand)}")
            print(f"Computers first card is {computers_hand[0]}")
            another = input("Type 'y' to get another card, type 'n' to pass: ")
            if(another == 'n'):
                another_card = False
            else:
                players_hand.append(deal_card())
                if (calculate_score(players_hand) > 21):
                    another_card = False

        # Forces the computer to pick a card if their total value is less than 17
        if (calculate_score(computers_hand) < 17):
            computers_hand.append(deal_card())

        # Calculate winner
        calculate_winner(players_hand, computers_hand)
        


        

