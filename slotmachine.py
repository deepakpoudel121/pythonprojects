MAX_LINES = 3

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

def main():
    balance = deposit()
    lines = number_lines()
    print(lines)
    print(balance)

main()