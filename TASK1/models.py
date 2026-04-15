from abc import ABC, abstractmethod
import datetime

class Transaction(ABC):  # Abstraction
    def __init__(self, amount: float, category: str, date=None):
        self.__amount = amount          # Encapsulation (private attribute)
        self.category = category
        self.date = date or datetime.date.today()

    @property
    def amount(self):                   # Getter (encapsulation)
        return self.__amount

    @abstractmethod
    def get_description(self):          # Polymorphism setup
        pass


class Income(Transaction):              # Inheritance
    def get_description(self):          # Polymorphism
        return f"Income: +${self.amount:.2f} from {self.category} ({self.date})"


class Expense(Transaction):             # Inheritance
    def get_description(self):          # Polymorphism
        return f"Expense: -${self.amount:.2f} on {self.category} ({self.date})"


class Budget:                           # Separate class for composition
    def __init__(self, category: str, limit: float):
        self.category = category
        self.limit = limit
        self.spent = 0.0

    def add_spending(self, amount: float):
        self.spent += amount

    def get_remaining(self) -> float:
        return self.limit - self.spent