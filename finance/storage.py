import json
import os
from .transaction import Transaction
def load_file(self):
    if not os.path.exists(self.filename):
         self.transactions = []
         return False
    try:
        with open(self.filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
            self.transactions = [Transaction.from_dict(item) for item in data]
    except (json.JSONDecodeError, FileNotFoundError):
        print("⚠️  Data file is corrupted or unreadable. Starting with an empty list.")
        self.transactions = []
        
def save_file(self):
    try:
        with open(self.filename, 'w', encoding='utf-8') as file:
            data = []
            for transaction in self.transactions:
                if hasattr(transaction, 'to_dict'):
                    data.append(transaction.to_dict())
                else:
                    data.append(transaction)
            json.dump(data, file, ensure_ascii=False, indent=2, default=str)
    except Exception as e:
        print(f"❌ Error saving file: {e}")
 