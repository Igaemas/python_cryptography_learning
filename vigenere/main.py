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
def rot13(character, key, list_of_character):
    position = list_of_character.find(character)
    new_position = (position + key) % len(list_of_character)
    new_character = list_of_character[new_position]
    return new_character

def rot13_selection(character, key):
    if character in number:
        return rot13(character, key, number)
    elif character.islower():
        return rot13(character, key, min_letter)
    elif character.isupper():
        return rot13()
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
                    vigenered_message_list.append(rot13_selection(character_to_rot, +int(rotation_key)))
                elif type == "decode":
                    vigenered_message_list.append(rot13_selection(character_to_rot, -int(rotation_key)))
                i += 1
    vigenered_message = "".join(vigenered_message_list)
    return vigenered_message

for arg in sys.argv :
    if "key:" in arg:
        key = (arg.split("key:"))[1]
    if "-h" == arg:
        print("key:<number> : your key for rotation (default : 13)\n-e : encode\n-d : decode\n-h : to display this message\n\nexemple : python3 main.py -e key:151 'test'\nexemple : python3 main.py -d key:151 'toij'")
        exit()
    if "-e" in arg:
        vigenere_type = "code"
    elif "-d" in arg:
        vigenere_type = "decode"
    else:
        message = arg

print(vigenere(message, key, vigenere_type))