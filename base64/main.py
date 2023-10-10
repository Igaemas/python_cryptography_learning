# python main.py -e "text to encode"
# python main.py -d "text to decode"

import re
import sys

base64_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
message = "hello"
test = "aGVsbG8"
crypted_message_list = []
binary_message_list = []
message_list = []

def is_six_multiple(binary_caracter):
    remainder = len(binary_caracter) % 6
    if remainder != 0:
        zero_to_add = 6 - remainder
        binary_caracter = binary_caracter + "0" * zero_to_add
    return binary_caracter

def to_base64(strings):
    binary_caracter = ''.join(format(ord(i), '08b') for i in strings)
    binary_ajusted = is_six_multiple(binary_caracter)
    group_of_six_binary_bits = re.findall('.{6}', binary_ajusted)
    for binary_bits in group_of_six_binary_bits:
        base10_caracter = int(binary_bits, 2)
        new_caracter = base64_alphabet[base10_caracter]
        crypted_message_list.append(new_caracter)
    crypted_message = "".join(crypted_message_list)
    return crypted_message

# ascii_character = []

def from_base64(crypted_message):
    for caracter in crypted_message:
        position = base64_alphabet.find(caracter)
        binary_message_list.append(format(position, '06b'))
    binary_octet_group = re.findall('.{8}', "".join(binary_message_list))
    for octet in binary_octet_group:
        decimal_value = int(octet, 2)
        message_list.append((chr(decimal_value)))
    clean_message = "".join(message_list)
    return clean_message
    
if sys.argv[1] == "-e":
    print(to_base64(sys.argv[2]))
elif sys.argv[1] == "-d":
    print(from_base64(sys.argv[2]))