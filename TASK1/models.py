from abc import ABC, abstractmethod
import datetime

class Transaction(ABC):  
    def __init__(self, amount: float, category: str, date=None):
        self.__amount = amount          
        self.category = category
        self.date = date or datetime.date.today()

    @property
    def amount(self):                   
        return self.__amount

    @abstractmethod
    def get_description(self):          
        pass


class Income(Transaction):              
    def get_description(self):          
        return f"Income: +${self.amount:.2f} from {self.category} ({self.date})"


class Expense(Transaction):           
    def get_description(self):         
        return f"Expense: -${self.amount:.2f} on {self.category} ({self.date})"


class Budget:                          
    def __init__(self, category: str, limit: float):
        self.category = category
        self.limit = limit
        self.spent = 0.0

    def add_spending(self, amount: float):
        self.spent += amount

    def get_remaining(self) -> float:
        return self.limit - self.spent
