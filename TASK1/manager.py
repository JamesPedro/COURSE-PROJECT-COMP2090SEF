from models import Income, Expense, Budget

class FinanceManager:
    def __init__(self):
        self.transactions = []          # List of Transaction objects
        self.budgets = {}               # Composition: category -> Budget object

    def add_transaction(self, transaction):
        self.transactions.append(transaction)
        if isinstance(transaction, Expense) and transaction.category in self.budgets:
            self.budgets[transaction.category].add_spending(transaction.amount)

    def set_budget(self, category: str, limit: float):
        self.budgets[category] = Budget(category, limit)

    def generate_report(self) -> str:
        total_income = sum(t.amount for t in self.transactions if isinstance(t, Income))
        total_expense = sum(t.amount for t in self.transactions if isinstance(t, Expense))
        return (f"Total Income : ${total_income:.2f}\n"
                f"Total Expenses: ${total_expense:.2f}\n"
                f"Net Balance  : ${total_income - total_expense:.2f}")

    def list_transactions(self) -> list:
        return [t.get_description() for t in self.transactions]

    def check_budgets(self) -> list:
        alerts = []
        for cat, budget in self.budgets.items():
            remaining = budget.get_remaining()
            if remaining < 0:
                alerts.append(f"⚠️  OVER BUDGET in {cat}! "
                              f"Spent ${budget.spent:.2f} / ${budget.limit:.2f}")
        return alerts or ["✅ All budgets are on track!"]