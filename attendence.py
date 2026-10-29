total = int(input("Enter total classes: "))
attended = int(input("Enter attended classes: "))

percentage = attended / total * 100

print("Attendance:", percentage, "%")

if percentage >= 75:
    print("Eligible")
else:
    print("Not eligible")

    