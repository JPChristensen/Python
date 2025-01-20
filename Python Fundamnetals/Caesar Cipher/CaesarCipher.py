#Global Variables
continue_cipher = True
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# def encode(message, adjust):
#     encoded_message = ""
#     alphabet_index_e = 0
#     for letter in message:
#         # Checks if there is a space for the character. 
#         if letter != " ":
#             alphabet_index_e = alphabet.index(letter) + adjust
#             # If index >= 26, subtract 26 from the number to start the index from 0
#             # if (alphabet_index >= len(alphabet)):
#             #     encoded_message += alphabet[(alphabet_index - len(alphabet))]
#             # else:
#             #     encoded_message += alphabet[alphabet_index]

#             # Easier way
#             alphabet_index_e %= len(alphabet) # 0-25
#             encoded_message += alphabet[alphabet_index_e]
#         else: 
#             encoded_message += " "
    
#     #Output encoded message
#     print(f"Here is your encoded message: {encoded_message}. \n")

# def decode(message, adjust):
#     decoded_message = ""
#     alphabet_index_d = 0
#     for letter in message:
#         if letter != " ":
#             alphabet_index_d = alphabet.index(letter) - adjust

#             alphabet_index_d %= len(alphabet)
#             decoded_message += alphabet[alphabet_index_d]
#         else:
#             decoded_message += " "

#     print(f"Here is your decoded message: {decoded_message}. \n")

# decode and encode combined into one function
def caesar(message, adjust, encode_decode):
    output_text = ""

    # Flips the sign of the shift to adjust positive or negative values 
    if (encode_decode == "decode"):
            adjust *= -1
    for letter in message:
        # Checks if the current letter is a space or a non-alphabetical character
        # If the letter is non-alpha it will just be appended to the string.
        if (letter != " " and letter.isalpha()):
            position_shift = alphabet.index(letter) + adjust
            position_shift %= len(alphabet)
            output_text += alphabet[position_shift]
        else:
            output_text += letter
        
    print(f"Here is your {encode_decode}d message: {output_text}. \n")
        

while continue_cipher:
    encode_decode = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower()
    if (encode_decode == "encode" or encode_decode == "decode"):
        text = input("Type your message: \n").lower()
        shift = int(input("Type the shift number: \n"))

        caesar(message=text, adjust=shift, encode_decode=encode_decode)
        
        cont = input("Would you like to go again? Y/N \n:").lower()
        if cont == "n":
            continue_cipher = False
    else:
        print("Invalid input. Try again.")
        continue_cipher = False
    

