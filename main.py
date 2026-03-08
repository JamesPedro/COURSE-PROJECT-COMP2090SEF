from abc import ABC, abstractmethod
import datetime

class Transaction(ABC):  
    def __init__(self, amount, category, date=None):
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
        return f"Income: +${self.amount} from {self.category}"

class Expense(Transaction):  
    def get_description(self):  
        return f"Expense: -${self.amount} on {self.category}"