def deposit():
    while True:
        amount = input("Enter the deposit amount: ")

        if amount.isdigit():  # ✅ check if numeric
            amount = int(amount)
            if amount > 0:   # ✅ positive check
                return amount
            else:
                print("❌ Amount must be greater than zero.")
        else:
            print("❌ Please enter a valid number.")

# --- usage ---
amount = deposit()
print(f"✅ Deposit successful: {amount}")
