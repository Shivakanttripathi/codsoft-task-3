
#PASSWORD GENERATOR CREATE BY ME.....

import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

length = int(input("Enter the length of the password: "))
password = generate_password(length)
print("Generated Password:", password)