
# Initialize an empty list to store expenses
expenses = []

# Function to add an expense
def add_expense():
    name = input("Enter expense name: ")
    amount = float(input("Enter expense amount: $"))
    expenses.append({"name": name, "amount": amount})
    print(f"{name} expense of ${amount:.2f} added successfully!")

# Function to view all expenses
def view_expenses():
    if not expenses:
        print("No expenses recorded yet.")
    else:
        print("Expense List:")
        for idx, expense in enumerate(expenses, start=1):
            print(f"{idx}. {expense['name']}: ${expense['amount']:.2f}")

# Main menu loop
while True:
    print("\nExpense Tracker Menu:")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Quit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        print("Exiting Expense Tracker. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
