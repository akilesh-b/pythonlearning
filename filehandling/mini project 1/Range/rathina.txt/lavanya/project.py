import pandas as pd
import matplotlib.pyplot as plt


expenses = [
    {"Date":"2026-06-01","Category":"Rent","Amount":12000,"Description":"House Rent"},
    {"Date":"2026-06-01","Category":"Grocery","Amount":850,"Description":"Vegetables"},
    {"Date":"2026-06-02","Category":"Fuel","Amount":1200,"Description":"Petrol"},
    {"Date":"2026-06-02","Category":"Gym","Amount":1500,"Description":"Gym Membership"},
    {"Date":"2026-06-03","Category":"Dining Out","Amount":900,"Description":"Restaurant"},
    {"Date":"2026-06-03","Category":"Shopping","Amount":2500,"Description":"Clothes"},
    {"Date":"2026-06-04","Category":"Bills","Amount":1800,"Description":"Electricity Bill"},
    {"Date":"2026-06-04","Category":"Medical","Amount":700,"Description":"Medicines"},
    {"Date":"2026-06-05","Category":"Insurance","Amount":3000,"Description":"Health Insurance"},
    {"Date":"2026-06-05","Category":"Travel","Amount":1500,"Description":"Bus Ticket"},

    {"Date":"2026-06-06","Category":"Deliveries","Amount":350,"Description":"Food Delivery"},
    {"Date":"2026-06-06","Category":"Savings","Amount":5000,"Description":"Savings Deposit"},
    {"Date":"2026-06-07","Category":"Investments","Amount":4000,"Description":"Mutual Fund SIP"},
    {"Date":"2026-06-07","Category":"Grocery","Amount":950,"Description":"Supermarket"},
    {"Date":"2026-06-08","Category":"Fuel","Amount":1300,"Description":"Petrol"},
    {"Date":"2026-06-08","Category":"Shopping","Amount":1800,"Description":"Shoes"},
    {"Date":"2026-06-09","Category":"Dining Out","Amount":1200,"Description":"Cafe"},
    {"Date":"2026-06-09","Category":"Bills","Amount":1000,"Description":"Internet Bill"},
    {"Date":"2026-06-10","Category":"Medical","Amount":1500,"Description":"Doctor Visit"},
    {"Date":"2026-06-10","Category":"Travel","Amount":2200,"Description":"Train Ticket"},

    {"Date":"2026-06-11","Category":"Rent","Amount":12000,"Description":"Apartment Rent"},
    {"Date":"2026-06-11","Category":"Fuel","Amount":1100,"Description":"Diesel"},
    {"Date":"2026-06-12","Category":"Grocery","Amount":1400,"Description":"Groceries"},
    {"Date":"2026-06-12","Category":"Gym","Amount":800,"Description":"Fitness Training"},
    {"Date":"2026-06-13","Category":"Shopping","Amount":3200,"Description":"Electronics"},
    {"Date":"2026-06-13","Category":"Deliveries","Amount":400,"Description":"Courier Charges"},
    {"Date":"2026-06-14","Category":"Insurance","Amount":2500,"Description":"Vehicle Insurance"},
    {"Date":"2026-06-14","Category":"Savings","Amount":6000,"Description":"Emergency Fund"},
    {"Date":"2026-06-15","Category":"Investments","Amount":5000,"Description":"Stocks"},
    {"Date":"2026-06-15","Category":"Dining Out","Amount":750,"Description":"Lunch"},

    {"Date":"2026-06-16","Category":"Bills","Amount":2200,"Description":"Water Bill"},
    {"Date":"2026-06-16","Category":"Travel","Amount":1700,"Description":"Cab Fare"},
    {"Date":"2026-06-17","Category":"Medical","Amount":600,"Description":"Medicines"},
    {"Date":"2026-06-17","Category":"Fuel","Amount":1400,"Description":"Petrol"},
    {"Date":"2026-06-18","Category":"Shopping","Amount":2100,"Description":"Accessories"},
    {"Date":"2026-06-18","Category":"Grocery","Amount":1300,"Description":"Vegetables"},
    {"Date":"2026-06-19","Category":"Gym","Amount":1000,"Description":"Workout Fees"},
    {"Date":"2026-06-19","Category":"Dining Out","Amount":1600,"Description":"Dinner"},
    {"Date":"2026-06-20","Category":"Deliveries","Amount":500,"Description":"Food Delivery"},
    {"Date":"2026-06-20","Category":"Savings","Amount":5500,"Description":"Savings Deposit"},

    {"Date":"2026-06-21","Category":"Investments","Amount":4500,"Description":"Mutual Fund SIP"},
    {"Date":"2026-06-21","Category":"Insurance","Amount":2800,"Description":"Health Insurance"},
    {"Date":"2026-06-22","Category":"Rent","Amount":12000,"Description":"House Rent"},
    {"Date":"2026-06-22","Category":"Bills","Amount":1900,"Description":"Electricity Bill"},
    {"Date":"2026-06-23","Category":"Fuel","Amount":1250,"Description":"Petrol"},
    {"Date":"2026-06-23","Category":"Travel","Amount":2400,"Description":"Train Ticket"},
    {"Date":"2026-06-24","Category":"Medical","Amount":1800,"Description":"Health Checkup"},
    {"Date":"2026-06-24","Category":"Shopping","Amount":2900,"Description":"Clothes"},
    {"Date":"2026-06-25","Category":"Grocery","Amount":1100,"Description":"Supermarket"},
    {"Date":"2026-06-25","Category":"Dining Out","Amount":950,"Description":"Cafe"},

    {"Date":"2026-06-26","Category":"Gym","Amount":1200,"Description":"Fitness Training"},
    {"Date":"2026-06-26","Category":"Deliveries","Amount":450,"Description":"Courier Charges"},
    {"Date":"2026-06-27","Category":"Savings","Amount":7000,"Description":"Emergency Fund"},
    {"Date":"2026-06-27","Category":"Investments","Amount":5500,"Description":"Stocks"},
    {"Date":"2026-06-28","Category":"Insurance","Amount":2600,"Description":"Vehicle Insurance"},
    {"Date":"2026-06-28","Category":"Bills","Amount":2100,"Description":"Internet Bill"},
    {"Date":"2026-06-29","Category":"Fuel","Amount":1350,"Description":"Diesel"},
    {"Date":"2026-06-29","Category":"Travel","Amount":1800,"Description":"Bus Ticket"},
    {"Date":"2026-06-30","Category":"Medical","Amount":900,"Description":"Medicines"},
    {"Date":"2026-06-30","Category":"Shopping","Amount":3500,"Description":"Electronics"},

    {"Date":"2026-07-01","Category":"Rent","Amount":12000,"Description":"House Rent"},
    {"Date":"2026-07-01","Category":"Grocery","Amount":1000,"Description":"Vegetables"},
    {"Date":"2026-07-02","Category":"Fuel","Amount":1200,"Description":"Petrol"},
    {"Date":"2026-07-02","Category":"Gym","Amount":1500,"Description":"Gym Membership"},
    {"Date":"2026-07-03","Category":"Dining Out","Amount":800,"Description":"Restaurant"},
    {"Date":"2026-07-03","Category":"Shopping","Amount":2200,"Description":"Clothes"},
    {"Date":"2026-07-04","Category":"Bills","Amount":1700,"Description":"Electricity Bill"},
    {"Date":"2026-07-04","Category":"Medical","Amount":650,"Description":"Medicines"},
    {"Date":"2026-07-05","Category":"Insurance","Amount":3000,"Description":"Health Insurance"},
    {"Date":"2026-07-05","Category":"Travel","Amount":1600,"Description":"Bus Ticket"},

    {"Date":"2026-07-06","Category":"Deliveries","Amount":400,"Description":"Food Delivery"},
    {"Date":"2026-07-06","Category":"Savings","Amount":5000,"Description":"Savings Deposit"},
    {"Date":"2026-07-07","Category":"Investments","Amount":4500,"Description":"Mutual Fund SIP"},
    {"Date":"2026-07-07","Category":"Grocery","Amount":1200,"Description":"Supermarket"},
    {"Date":"2026-07-08","Category":"Fuel","Amount":1400,"Description":"Petrol"},
    {"Date":"2026-07-08","Category":"Shopping","Amount":2800,"Description":"Shoes"},
    {"Date":"2026-07-09","Category":"Dining Out","Amount":1100,"Description":"Cafe"},
    {"Date":"2026-07-09","Category":"Bills","Amount":1200,"Description":"Internet Bill"},
    {"Date":"2026-07-10","Category":"Medical","Amount":1400,"Description":"Doctor Visit"},
    {"Date":"2026-07-10","Category":"Travel","Amount":2500,"Description":"Train Ticket"},

    {"Date":"2026-07-11","Category":"Rent","Amount":12000,"Description":"Apartment Rent"},
    {"Date":"2026-07-11","Category":"Fuel","Amount":1100,"Description":"Diesel"},
    {"Date":"2026-07-12","Category":"Grocery","Amount":1500,"Description":"Groceries"},
    {"Date":"2026-07-12","Category":"Gym","Amount":900,"Description":"Workout Fees"},
    {"Date":"2026-07-13","Category":"Shopping","Amount":3100,"Description":"Electronics"},
    {"Date":"2026-07-13","Category":"Deliveries","Amount":450,"Description":"Courier Charges"},
    {"Date":"2026-07-14","Category":"Insurance","Amount":2700,"Description":"Vehicle Insurance"},
    {"Date":"2026-07-14","Category":"Savings","Amount":6000,"Description":"Emergency Fund"},
    {"Date":"2026-07-15","Category":"Investments","Amount":5200,"Description":"Stocks"},
    {"Date":"2026-07-15","Category":"Dining Out","Amount":900,"Description":"Dinner"},

    {"Date":"2026-07-16","Category":"Bills","Amount":2000,"Description":"Water Bill"},
    {"Date":"2026-07-16","Category":"Travel","Amount":1900,"Description":"Cab Fare"},
    {"Date":"2026-07-17","Category":"Medical","Amount":750,"Description":"Medicines"},
    {"Date":"2026-07-17","Category":"Fuel","Amount":1300,"Description":"Petrol"},
    {"Date":"2026-07-18","Category":"Shopping","Amount":2600,"Description":"Accessories"},
    {"Date":"2026-07-18","Category":"Grocery","Amount":1350,"Description":"Vegetables"},
    {"Date":"2026-07-19","Category":"Gym","Amount":1100,"Description":"Fitness Training"},
    {"Date":"2026-07-19","Category":"Dining Out","Amount":1500,"Description":"Dinner"},
    {"Date":"2026-07-20","Category":"Deliveries","Amount":550,"Description":"Food Delivery"},
    {"Date":"2026-07-20","Category":"Savings","Amount":6500,"Description":"Savings Deposit"}
  
]

categories = [
    "Rent", "Gym", "Grocery", "Travel", "Dining Out",
    "Shopping", "Bills", "Medical", "Insurance",
    "Fuel", "Deliveries", "Savings", "Investments"
]

while True:

    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Monthly Report")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        date = input("Enter Date (YYYY-MM-DD): ")

        print("\nCategories:")
        for i, category in enumerate(categories, start=1):
            print(f"{i}. {category}")

        cat_choice = int(input("Choose Category Number: "))

        if 1 <= cat_choice <= len(categories):

            category = categories[cat_choice - 1]

            amount = float(input("Enter Amount: "))
            description = input("Enter Description: ")

            expenses.append({
                "Date": date,
                "Category": category,
                "Amount": amount,
                "Description": description
            })

            print("Expense Added Successfully!")

        else:
            print("Invalid Category Number!")

    elif choice == "2":

        df = pd.DataFrame(expenses)

        print("\n===== ALL EXPENSES =====")
        print(df)

    elif choice == "3":

        month = input("Enter Month (YYYY-MM): ")

        df = pd.DataFrame(expenses)

        monthly_df = df[df["Date"].str.startswith(month)]

        if monthly_df.empty:
            print("No expenses found for this month.")

        else:

            print("\n===== MONTHLY REPORT =====")
            print(monthly_df)

            total = monthly_df["Amount"].sum()

            print("\nTotal Expenses:", total)

            category_summary = (
                monthly_df
                .groupby("Category")["Amount"]
                .sum()
                .sort_values(ascending=False)
            )

            print("\n===== CATEGORY WISE SUMMARY =====")
            print(category_summary)

            plt.figure(figsize=(8, 8))

            plt.pie(
                category_summary,
                labels=category_summary.index,
                autopct="%1.1f%%",
                startangle=90
            )

            plt.title(f"Expense Distribution - {month}")

            plt.axis("equal")

            plt.show()

    elif choice == "4":

        print("Thank You For Using Expense Tracker!")
        break

    else:
        print("Invalid Choice!")