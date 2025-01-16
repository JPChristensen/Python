logo = """                         ___________
                                  /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-'''---------'' '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\""""

more_bidders = True
bidders = {
    'Name': [],
    'Bid': [],
}

print(logo)

def find_highest_bidder(bidding_dictionary):
        # Initializes a sequence containing an empty string for name and an integer space for bid, to store for highest bid
        highest_bidder = ["", 0]
        # Counts interations through the for loop to determine which position the value was higher, than assigns those values to highest_bidder
        counter = 0
        for value in bidders["Bid"]:
            # Compares the Bid value against the Bid index of highest_bidder, if it is bigger, the values Name and Bid are stored in highest bidder.
            if (value > highest_bidder[1]):
                highest_bidder[0] = bidders["Name"][counter]
                highest_bidder[1] = bidders["Bid"][counter]
            counter += 1
        # Prints highest bidder name and bid.
        print(f"The winner is {highest_bidder[0]} with a bid of ${highest_bidder[1]}.")
    
# Loop while more bidders
while more_bidders:
    bidders["Name"].append(input("What is your name?:  "))
    bidders["Bid"].append(int(input("What is your bid?  $")))

    if (input("Are there any other bidders? Type 'yes' or 'no':  ").lower() == "yes"):
        # Clears the terminal to keep bidding values a secret
        print("\n" * 100)
    else:
        more_bidders = False
        find_highest_bidder(bidders)
        
