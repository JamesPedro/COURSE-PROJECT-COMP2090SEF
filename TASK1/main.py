from models import Income, Expense
from manager import FinanceManager
from storage import DataStorage

def main():
    manager = FinanceManager()
    storage = DataStorage()
    storage.load(manager)                     # Load previous data if exists

    print("=== Personal Finance Tracker ===\n")

    while True:
        print("\n1. Add Income")
        print("2. Add Expense")
        print("3. Set Budget")
        print("4. View Report")
        print("5. List All Transactions")
        print("6. Check Budgets")
        print("7. Save & Exit")
        choice = input("Choose an option (1-7): ")

        if choice == '1':
            amt = float(input("Amount: "))
            cat = input("Category (e.g. Salary): ")
            manager.add_transaction(Income(amt, cat))
            print("Income added!")
        elif choice == '2':
            amt = float(input("Amount: "))
            cat = input("Category (e.g. Food): ")
            manager.add_transaction(Expense(amt, cat))
            print("Expense added!")
        elif choice == '3':
            cat = input("Category: ")
            limit = float(input("Monthly limit: "))
            manager.set_budget(cat, limit)
            print(f"Budget for {cat} set to ${limit:.2f}")
        elif choice == '4':
            print("\n" + manager.generate_report())
        elif choice == '5':
            print("\nTransactions:")
            for desc in manager.list_transactions():
                print("  " + desc)
        elif choice == '6':
            for alert in manager.check_budgets():
                print(alert)
        elif choice == '7':
            storage.save(manager)
            print("Data saved. Goodbye!")
            break
        else:
            print("Invalid option, try again.")

if __name__ == "__main__":
    main()
