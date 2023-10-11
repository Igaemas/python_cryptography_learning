import sys
import re

message = ""
key = "538"
vigenered_message_list = []

# list of caracter
min_letter = "abcdefghijklmnopqrstuvwxyz"
max_letter = min_letter.upper()
number = "0123456789"

# function
def rot13(character, key):
    if character in number:
        position = number.find(character)
        new_position = (position + key) % 10
        new_character = number[new_position]
        return new_character
    elif character.islower():
        position = min_letter.find(character)
        new_position = (position + key) % 26
        new_character = min_letter[new_position]
        return new_character
    elif character.isupper():
        position = max_letter.find(character) % 26
        new_position = position + key
        new_character = max_letter[new_position]
        return new_character
    elif character == " ":
            return " "


def vigenere(message, key, type):
    message_in_group_of_k_bloc = re.findall('.{1,3}', message)
    for bloc in range(1,len(message_in_group_of_k_bloc)+1):
        i = 0
        for rotation_key in key :
            if i < len(message_in_group_of_k_bloc[bloc-1]):
                character_to_rot = (message_in_group_of_k_bloc[bloc-1])[int(i)]
                if type == "code":
                    vigenered_message_list.append(rot13(character_to_rot, +int(rotation_key)))
                elif type == "decode":
                    vigenered_message_list.append(rot13(character_to_rot, -int(rotation_key)))
                i += 1
    vigenered_message = "".join(vigenered_message_list)
    return vigenered_message

for arg in sys.argv :
    if "key:" in arg:
        key = (arg.split("key:"))[1]
    if "-h" == arg:
        print("key:<number> : your key for rotation (default : 13)\n-h : to display this message\n\nexemple : python3 main.py key:15 'test'")
        exit()
    if "-e" in arg:
        vigenere_type = "code"
    elif "-d" in arg:
        vigenere_type = "decode"
    else:
        message = arg

print(vigenere(message, key, vigenere_type))