import random

MAX_BET = 100
MIN_BET = 1
MAX_LINES = 3

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2, 
    "B": 4,
    "C": 6, 
    "D": 8 
}

symbol_value = {
    "A": 5, 
    "B": 4,
    "C": 3, 
    "D": 2 
}

def check_winning(columns, lines, bet, values):
    winning = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winning += values[symbol] * bet
            winning_lines.append(line + 1)

    return winning, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    
    columns = []
    for _ in range(cols):
        column = []
        current_symbol = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbol)
            current_symbol.remove(value)
            column.append(value)

        columns.append(column)

    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) -1:
                print(column[row], end="|")
            else:
                print(column[row], end="")
        print()

def deposit():
    while True:
        try:
            amount = int(input("How much would you like to deposit? $"))
            if amount > 0:
                break
            else:
                print("Enter a number greater than 0.")

        except ValueError:
            print("Please enter a number.")

    return amount
        
def get_line():
    while True:
        try:
            lines = int(input(f"Enter the number of lines to bet on (1 - {MAX_LINES}): "))
            if MIN_BET <= lines <= MAX_LINES:
                break
            else:
                print(f"Enter a number between ({MIN_BET} - {MAX_LINES})")

        except ValueError:
            print("Please enter a number.")

    return lines
        
def get_bet():
    while True:
        try:
            amount = int(input(f"How much you would like to bet on each line? $"))
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} and ${MAX_BET}.")

        except ValueError:
            print("Please enter a number.")

    return amount

def spin(balance):
    lines = get_line()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if balance < total_bet:
            print(f"Oops, Insufficient Balance. Balance: {balance}")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet = {total_bet}")

    slot = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slot)
    winning, winning_lines = check_winning(slot, lines, bet, symbol_value)
    print(f"You Won ${winning}.")
    print(f"You Won on lines:", *winning_lines)
    return winning - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current Balance: {balance}")
        answer = input("Press enter to play or (q for quit)")
        if answer.lower() == "q":
            break
        balance += spin(balance)

    print(f"You left with ${balance}")    
main()