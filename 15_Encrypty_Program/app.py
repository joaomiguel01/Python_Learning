import random
import string

chars = ' ' + string.punctuation + string.digits + string.ascii_letters

chars = list(chars)
key = chars.copy()
random.shuffle(key)

# ENCRYPT
plain_text = input("Enter a message to encrypt: ")
cipher_text = ""

for l in plain_text:
    index = chars.index(l)
    cipher_text += key[index]

print(f"Original Message: {plain_text}")
print(f"Encrypt Message : {cipher_text}")

# DESENCRYPT
cipher_text = input("Enter a message to desencrypt: ")
plain_text = ""

for l in cipher_text:
    index = key.index(l)
    plain_text += chars[index]

print(f"Encrypt Message : {cipher_text}")
print(f"Original Message: {plain_text}")
