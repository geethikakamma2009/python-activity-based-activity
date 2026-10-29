balance = 5000

amount = int(input("Enter amount: "))
choice = input("Enter D for deposit or W for withdrawal: ")

if choice == "D":
    balance = balance + amount
elif choice == "W":
    if amount <= balance:
        balance = balance - amount
    else:
        print("Insufficient balance")

print("Final balance:", balance)