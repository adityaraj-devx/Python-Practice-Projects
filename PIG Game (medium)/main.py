import random


def dice_roll():
    min_value = 1
    max_value = 6
    dice_point = random.randint(min_value, max_value)
    return dice_point


while True:
    try:
        players = int(input("Enter number of players (2-4): "))
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 - 4 players.")
    except ValueError:
        print("Invalid, try again.")

max_score = 50
players_score = [0 for _ in range(players)]

while max(players_score) < max_score:
    for player_idx in range(players):
        print(f"\nPlayer number {player_idx + 1} turn has just started.\n")
        print(f"Your total score is {players_score[player_idx]}.\n")
        current_score = 0

        while True:
            roll = input("Would you like to roll? (y/n): ").lower()
            if roll != "y":
                break

            value = dice_roll()

            if value == 1:
                print("You rolled a 1! Your turn is over!")
                current_score = 0
                break
            else:
                current_score += value
                print(f"You rolled a: {value}")

            print(f"Your score is: {current_score}")

        players_score[player_idx] += current_score
        print(f"Your total score is {players_score[player_idx]}")

max_score = max(players_score)
winning_player = players_score.index(max_score)
print(f"Player number {winning_player + 1} won with a score of {max_score}")
