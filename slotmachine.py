
import random


MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1
ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

def get_slot_machine_spin(rows,cols,symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(all_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end= " | ")
            else:
                print(column[row], end= "")
        print()

def deposit():
    while True:
        amount = input("Enter the deposit amount: $")

        if amount.isdigit():  
            amount = int(amount)
            if amount > 0:   
                return amount
            else:
                print("❌ Amount must be greater than zero.")
        else:
            print("❌ Please enter a valid number.")


def number_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1 - " + str(MAX_LINES) +
        "): ")

        if lines.isdigit():  
            lines = int(lines)
            if lines > 0 and lines <= MAX_LINES:   
                return lines
            else:
                print("❌ Lines must be greater than zero and Less or equal to " + str(MAX_LINES))
        else:
            print("❌ Please enter a valid lines number.")

def get_bet():
    while True:
        amount = input("How much would you like to bet on each line : $")

        if amount.isdigit():  
            amount = int(amount)
            if amount > 0:   
                return amount
            else:
                print(f"❌ Amount must be between ${MIN_BET} - ${MAX_BET}")
        else:
            print("❌ Please enter a valid bet.")

def main():
    balance = deposit()
    lines = number_lines()
   
    
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print("Not enough balance. Your balance is" + str(balance))
        else:
            break
        
    print(f"You are betting ${bet} on {lines} lines. Total bet is {total_bet} ")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)















main()