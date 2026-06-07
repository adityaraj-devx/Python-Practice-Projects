import random

number_range = int(input("Type a number: "))
if number_range <= 0:
    print("Please type a number larger than 0 next time.")
    quit()

random_number = random.randint(0, number_range)
guesses = 0

while True:
    guesses += 1
    guess = int(input("Mkae a guess: "))
    if guess <= 0:
        print("Please type a number larger than 0 next time.")
        continue
    if guess == random_number:
        print("You got it!")
        break
    elif guess > random_number:
        print("You were above the number,")
    else:
        print("You were below the number,")
print(f"You got it in {guesses} guesses.")