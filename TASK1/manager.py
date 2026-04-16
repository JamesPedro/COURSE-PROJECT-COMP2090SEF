from models import Income, Expense, Budget

class FinanceManager:                        # Creates the main class that controls everything.
    def __init__(self):
        self.transactions = []               # list of Transaction objects
        self.budgets = {}                    # dictionary of Budget objects

    def add_transaction(self, transaction):
        self.transactions.append(transaction)
        if isinstance(transaction, Expense) and transaction.category in self.budgets:        # it is an Expense and we have a budget for that category, automatically update the spent amount.
            self.budgets[transaction.category].add_spending(transaction.amount)

    def set_budget(self, category, limit):
        self.budgets[category] = Budget(category, limit)

    def generate_report(self):               # calculates total income, expenses and net balance
        total_income = 0
        total_expense = 0
        for t in self.transactions:
            if isinstance(t, Income):
                total_income = total_income + t.amount
            if isinstance(t, Expense):
                total_expense = total_expense + t.amount
        net = total_income - total_expense
        return "Total Income : " + str(total_income) + "\nTotal Expenses: " + str(total_expense) + "\nNet Balance  : " + str(net)

    def list_transactions(self):
        result = []
        for t in self.transactions:
            result.append(t.get_description())
        return result

    def check_budgets(self):                # Checks every budget. If overspent, adds a warning message.
        alerts = []
        for cat, b in self.budgets.items():
            remaining = b.get_remaining()
            if remaining < 0:
                alerts.append("OVER BUDGET in " + cat + "! Spent " + str(b.spent) + " / " + str(b.limit))
        if alerts == []:
            alerts.append("All budgets are on track!")
        return alerts
