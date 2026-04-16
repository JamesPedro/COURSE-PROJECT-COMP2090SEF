class Transaction:
    def __init__(self, amount, category, date=None):
        self.amount = amount
        self.category = category
        self.date = date   

    def get_description(self):
        pass  


class Income(Transaction):
    def get_description(self):
        return "Income: +" + str(self.amount) + " from " + self.category


class Expense(Transaction):
    def get_description(self):
        return "Expense: -" + str(self.amount) + " on " + self.category


class Budget:
    def __init__(self, category, limit):
        self.category = category
        self.limit = limit
        self.spent = 0

    def add_spending(self, amount):
        self.spent = self.spent + amount

    def get_remaining(self):
        return self.limit - self.spent
