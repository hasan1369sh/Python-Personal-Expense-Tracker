def remove_transaction(self, index):
    if not 0 <= index <= len(self.transactions):
        print('\nNot Found')
        return False
    removed_transaction = self.transactions.pop(index)
    self.save_file()
    print("\nSuccessfull")
    return True