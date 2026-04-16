import json
import datetime
from models import Income, Expense

class DataStorage:
    def save(self, manager, filename='finance_data.json'):
        data = {
            'transactions': [],
            'budgets': {cat: {'limit': b.limit, 'spent': b.spent}
                        for cat, b in manager.budgets.items()}
        }
        for t in manager.transactions:
            data['transactions'].append({
                'type': 'Income' if isinstance(t, Income) else 'Expense',
                'amount': t.amount,
                'category': t.category,
                'date': str(t.date)
            })
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)

    def load(self, manager, filename='finance_data.json'):
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
            manager.transactions = []
            for t in data.get('transactions', []):
                date = datetime.datetime.strptime(t['date'], '%Y-%m-%d').date()
                if t['type'] == 'Income':
                    trans = Income(t['amount'], t['category'], date)
                else:
                    trans = Expense(t['amount'], t['category'], date)
                manager.add_transaction(trans)
            manager.budgets = {}
            for cat, b in data.get('budgets', {}).items():
                manager.set_budget(cat, b['limit'])
                manager.budgets[cat].spent = b['spent']
            return True
        except FileNotFoundError:
            return False
