# Python Encryption Game

from random import shuffle
import string

chars = ' ' + string.punctuation + string.ascii_letters + string.digits
chars = list(chars)
key = chars.copy()

shuffle(key)

# print(f"chars: {chars}")
# print(f"key: {key}")

# ENCRYPT
plain_text = input("Enter a message to encrypt: ")
cipher_text = ""

for letter in plain_text:
    cipher_text += key[chars.index(letter)]

print(f"Original Message:", plain_text)
print(f"Encrypted Message:", cipher_text)

# DECRYPT
cipher_text = input("Enter a message to encrypt: ")
plain_text = ""

for letter in cipher_text:
    plain_text += chars[key.index(letter)]

print(f"Encrypted Message:", cipher_text)
print(f"Original Message:", plain_text)
