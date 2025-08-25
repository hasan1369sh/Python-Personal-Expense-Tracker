def edit_transaction(self, index, new_transaction):
        if not 0 <= index <= len(self.transactions):
            print('\n Not Found !!!')
            return False
        transaction = self.transactions[index]
        if 'amount' in new_transaction and new_transaction['amount'].strip():
            transaction.amount = new_transaction['amount'].strip()
        if 'category' in new_transaction and new_transaction['category'].strip():
            transaction.category = new_transaction['category'].strip()
        if 'date' in new_transaction and new_transaction['date'].strip():
            transaction.date = new_transaction['date'].strip()
        if 'type' in new_transaction and new_transaction['type'].strip():
            transaction.type = new_transaction['type'].strip()
        if 'description' in new_transaction and new_transaction['description'].strip():
            transaction.description = new_transaction['description'].strip()
        self.save_file()
        print('\nSuccessfully')
        return True