import random

user_win = 0
computer_win = 0

options = ["rock", "paper", "scissor"]

while True:
    user_input = input("Type Rock/Paper/Scissor or Q to quit the game: ").lower()

    if user_input == "q":
        break
    if user_input not in options:
        continue

    rnadom_number = random.randint(0, 2)
    computer_pick = options[rnadom_number]

    print(f"Computer picked : {computer_pick}")

    if user_input == computer_pick:
        print("Tied!")
    elif user_input == "rock" and computer_pick == "scissor":
        print("You won!")
        user_win += 1
    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_win += 1
    elif user_input == "scissor" and computer_pick == "paper":
        print("You won!")
        user_win += 1
    else:
        print("Computer Won!")
        computer_win += 1

print(f"You won {user_win} times.")
print(f"You won {computer_win} times.")

print("Goodbye!!!!!")