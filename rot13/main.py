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

# list of character
min_letter = "abcdefghijklmnopqrstuvwxyz"
max_letter = min_letter.upper()
number = "0123456789"

# futur message var
new_message_list = []
new_message = ""

def rot13(character, key, list_of_character):
    position = list_of_character.find(character)
    new_position = (position + key) % len(list_of_character)
    new_character = list_of_character[new_position]
    new_message_list.append(new_character)

def main(message, key):
    message_list = list(message)
    for character in message_list:
        if character in number:
            rot13(character, key, number)
        if character.islower():
            rot13(character, key, min_letter)
        if character.isupper():
            rot13(character, key, max_letter)
        if character == " ":
            new_message_list.append(" ")
    message_list = "".join(new_message_list)
    return(message_list)

print(main(message, rotation_key))