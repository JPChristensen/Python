logo = '''
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ '.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ '.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   '._____.'  | || ||____|  |____|| || |  |________|  | || |   '._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|'''

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

# Prints the possible operations and returns the user's choice.
def show_operations():
    for key in opertaions:
        print(key)

    return input("What operation do you want to use?:  ")

# Keep Calculating
cont = True

while cont:
    print(logo)
    first_number = float(input("What is your first number?:  "))
    same_operation = True

    # If the user would like to continue the operations
    while same_operation:
        user_operation = show_operations()
        second_number = float(input("What is your second number?:  "))
        
        
        answer = opertaions[user_operation](first_number,second_number)
        print(f"{first_number} {user_operation} {second_number} = {answer}")

        keep_going = input(f"Type 'y' to continue calculating with {answer}, type 'n' to start a new calculation, or type anything else to quit application:  ")

        #Continues the loop based on the user's selection, y for the same equation, n for a new equation, or anything else to quit the application.
        if (keep_going == 'y'):
            first_number = answer
        elif (keep_going == 'n'):
            same_operation = False
        else:
            cont = False
            same_operation = False
            
    