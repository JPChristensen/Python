#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

#Adds the amount of characters the user inputted by using a for loop XYZ amount of times using the random.choice method for sequences

# new_password = ""

# for x in range(1, nr_letters + 1):
#     new_password += random.choice(letters)

# for y in range(1, nr_symbols +1):
#     new_password += random.choice(symbols)

# for z in range(1, nr_numbers + 1):
#     new_password += random.choice(numbers)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

new_password = []

for x in range(1, nr_letters + 1):
    new_password.append(random.choice(letters))

for y in range(1, nr_symbols +1):
    new_password.append(random.choice(symbols))

for z in range(1, nr_numbers + 1):
    new_password.append(random.choice(numbers))

#Using the shuffle function from Random, we shuffle the newly created sequence and then convert it back into a string and storing it in secure_password.
secure_password = ""
random.shuffle(new_password)
for char in new_password:
    secure_password += char

print(secure_password)