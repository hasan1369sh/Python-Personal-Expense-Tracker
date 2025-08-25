from .transaction import Transaction        
FILENAME = 'data/transaction.json'
        
class TransactionList():
    def __init__(self, filename = FILENAME):
        self.filename = filename
        self.transactions = []
        self.load_file()
    
    def load_file(self):
        from .storage import load_file
        load_file(self)    
    
    def save_file(self):
        from .storage import save_file
        save_file(self)
           
    def add(self,type):
        from services import add
        add.insert_transaction(self, Transaction, type)  
      
    def display(self):
        from services import display
        display.diplay_transactions(self)
               
    def searches(self, query):
        from services import search
        return search.search_result(self, query)
        
    def edit(self, index, new_transaction):
        from services import edit
        edit.edit_transaction(self, index, new_transaction)
    
    def remove(self, index):
        from services import remove
        remove.remove_transaction(self, index)
    
    def filter_item(self, time_frame):
        from services import filter
        return filter.filtered_item(self, time_frame)
            
    def reports(self, time_frame, category_selected='all'):
        from services import report
        report.get_report(self, time_frame, category_selected)
            