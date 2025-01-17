

"""Operation Function"""

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

opertaions = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

cont = True
while cont:
    first_number = int(input("What is your first number?:  "))
    second_number = int(input("What is your second number?:  "))
    user_operation = input("What operation do you want to use?:  ")
    

    print(f"{first_number} {user_operation} {second_number} = {opertaions[user_operation](first_number,second_number)}")