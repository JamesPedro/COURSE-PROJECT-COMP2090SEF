import json

class DataStorage:
    def save(self, manager, filename='finance_data.json'):                 # saves all transactions and budgets to JSON file
        data = {
            'transactions': [],
            'budgets': {}
        }
        for t in manager.transactions:
            data['transactions'].append({
                'type': 'Income' if isinstance(t, Income) else 'Expense',
                'amount': t.amount,
                'category': t.category
            })
        for cat, b in manager.budgets.items():
            data['budgets'][cat] = {'limit': b.limit, 'spent': b.spent}
        with open(filename, 'w') as f:
            json.dump(data, f)

    def load(self, manager, filename='finance_data.json'):                  # loads data back and recreates objects
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
            manager.transactions = []
            for t in data.get('transactions', []):
                if t['type'] == 'Income':
                    trans = Income(t['amount'], t['category'])
                else:
                    trans = Expense(t['amount'], t['category'])
                manager.add_transaction(trans)
            manager.budgets = {}
            for cat, b in data.get('budgets', {}).items():
                manager.set_budget(cat, b['limit'])
                manager.budgets[cat].spent = b['spent']
            return True
        except:
            return False
