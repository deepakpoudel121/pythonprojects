
def deposit():
    while True:
        amount = input("Enter the amount you would like to deposit: $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                return amount
            else:
                print("Amount must be greater than zero")
        else:
            print("Enter a valid amount")

def main():
    balance = deposit()
    print(balance)


main()