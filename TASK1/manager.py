from models import Income, Expense, Budget

class FinanceManager:
    def __init__(self):
        self.transactions = []
        self.budgets = {}

    def add_transaction(self, transaction):
        self.transactions.append(transaction)
        if isinstance(transaction, Expense) and transaction.category in self.budgets:
            self.budgets[transaction.category].add_spending(transaction.amount)

    def set_budget(self, category, limit):
        self.budgets[category] = Budget(category, limit)

    def generate_report(self):
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

    def check_budgets(self):
        alerts = []
        for cat, b in self.budgets.items():
            remaining = b.get_remaining()
            if remaining < 0:
                alerts.append("OVER BUDGET in " + cat + "! Spent " + str(b.spent) + " / " + str(b.limit))
        if alerts == []:
            alerts.append("All budgets are on track!")
        return alerts
