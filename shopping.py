budget = int(input("Enter your budget: "))
price = int(input("Enter shopping cost: "))

if price <= budget:
    print("Shopping is within budget")
else:
    print("Budget exceeded")