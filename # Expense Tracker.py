# Expense Tracker

expenses = {}

while True:
    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Category-wise Expenses")
    print("4. Total Expense")
    print("5. Monthly Report")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        date = input("Enter Date (YYYY-MM-DD): ")
        category = input("Enter Category: ")
        amount = float(input("Enter Amount: "))

        if category not in expenses:
            expenses[category] = []

        expenses[category].append((date, amount))

        file = open("expenses.txt", "a")
        file.write(f"{date},{category},{amount}\n")
        file.close()

        print("Expense Added Successfully!")

    elif choice == "2":
        print("\nAll Expenses")
        for category in expenses:
            for date, amount in expenses[category]:
                print(date, "-", category, "- ₹", amount)

    elif choice == "3":
        print("\nCategory-wise Expenses")
        for category in expenses:
            total = 0
            for date, amount in expenses[category]:
                total += amount
            print(category, ":", total)

    elif choice == "4":
        total = 0
        for category in expenses:
            for date, amount in expenses[category]:
                total += amount
        print("Total Expense = ₹", total)

    elif choice == "5":
        month = input("Enter Month (YYYY-MM): ")
        total = 0
        print("\nMonthly Report")
        for category in expenses:
            for date, amount in expenses[category]:
                if date.startswith(month):
                    print(date, "-", category, "- ₹", amount)
                    total += amount
        print("Monthly Total = ₹", total)

    elif choice == "6":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")