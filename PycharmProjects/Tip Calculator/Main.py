# Code Below

print("Welcome to the tip calculator!")

amount = int(input("What was the total bill? "))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
num_of_people = int(input("How many people split the bill? "))
total = ((amount + (amount * tip/100)) / num_of_people)
print("Each person should pay: " + str(round(total,2)))