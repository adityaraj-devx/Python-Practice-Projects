import random
import string

def generate_password(length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters

    if numbers:
        characters += digits
    if special_characters:
        characters += special

    pwd = ""
    meet_criteria = False
    has_digit = False
    has_special = False

    while not meet_criteria or len(pwd) < length:
        char = random.choice(characters)
        pwd += char

        if char in digits:
            has_digit = True
        if char in special:
            has_special = True

        meet_criteria = True

        if numbers:
            meet_criteria = meet_criteria and has_digit

        if special_characters:
            meet_criteria = meet_criteria and has_special

    return pwd


length = int(input("Length of password: "))
has_digit = input("Do you want to add number in the password? (y/n): ").lower() == "y"
has_special = input("Do you want to add special characters in the password? (y/n): ").lower() == "y"

pwd = generate_password(length, has_digit, has_special)
print(f"The generated password: {pwd}")