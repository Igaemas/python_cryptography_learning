import sys

rotation_key = 13

for arg in sys.argv :
    if "key:" in arg:
        rotation_key = int((arg.split("key:"))[1])
    if "-h" == arg:
        print("key:<number> : your key for rotation (default : 13)\n-h : to display this message\n\nexemple : python3 main.py key:15 'test'")
        exit()
    else:
        message = arg

# list of caracter
min_letter = "abcdefghijklmnopqrstuvwxyz"
max_letter = min_letter.upper()
number = "0123456789"

# futur message var
new_message_list = []
new_message = ""

# function
def rot13(message, key):
    message_list = list(message)
    for caracter in message_list:
        if caracter in number:
            position = number.find(caracter)
            new_position = (position + key) % 10
            new_caracter = number[new_position]
            new_message_list.append(new_caracter)
        if caracter.islower():
            position = min_letter.find(caracter)
            new_position = (position + key) % 26
            new_caracter = min_letter[new_position]
            new_message_list.append(new_caracter)
        if caracter.isupper():
            position = max_letter.find(caracter) % 26
            new_position = position + key
            new_caracter = max_letter[new_position]
            new_message_list.append(new_caracter)
        if caracter == " ":
            new_message_list.append(" ")
    message_list = "".join(new_message_list)
    print(message_list)

rot13(message, rotation_key)