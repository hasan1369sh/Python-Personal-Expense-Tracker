
FILENAME = 'data/transaction.json'

class Transaction():
    def __init__(self, amount, category, date, description, type):
        self.amount = amount
        self.category = category
        self.date = date
        self.description = description
        self.type = type
    
    def __str__(self):
        return f"{self.category} : {self.amount} - {self.type} - {self.date} - {self.description}"
    
    def __repr__(self):
        return f"Transaction(category={self.category}, amount={self.amount}, date={self.date}, type={self.type}, description={self.description})"
    
    def to_dict(self):
        return {
            'amount': self.amount,
            'category': self.category,
            'date': self.date,
            'description': self.description,
            'type': self.type
        }
        
    @staticmethod
    def from_dict(data):
        return Transaction(data['amount'], data['category'], data['date'], data['description'], data['type'])
        
        
class TransactionList():
    def __init__(self, filename = FILENAME):
        self.filename = filename
        self.transactions = []
        self.load_file()
    
    def load_file(self):
        from . import storage
        storage.load_file(self)    
    
    def save_file(self):
        from . import storage
        storage.save_file(self)
           
    def add(self,type):
        from . import add
        add.insert_transaction(self, Transaction, type)  
      
    def display(self):
        from . import display
        display.diplay_transactions(self)
               
    def searches(self, query):
        from . import search
        return search.search_result(self, query)
        
    def edit(self, index, new_transaction):
        from . import edit
        edit.edit_transaction(self, index, new_transaction)
    
    def remove(self, index):
        from . import remove
        remove.remove_transaction(self, index)
    
    def filter_item(self, time_frame):
        from . import filter
        return filter.filtered_item(self, time_frame)
            
    def reports(self, time_frame, category_selected='all'):
        from . import report
        report.get_report(self, time_frame, category_selected)
            