distance = int(input("Enter distance in km: "))
mileage = int(input("Enter mileage: "))
price = int(input("Enter fuel price: "))

fuel = distance / mileage
cost = fuel * price

print("Fuel required:", fuel)
print("Fuel cost:", cost)