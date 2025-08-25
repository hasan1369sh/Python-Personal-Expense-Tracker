def diplay_transactions(self):
    if len(self.transactions) == 0:
        print('Empty List ...')
    else:
        for i, transaction in enumerate(self.transactions):
            print(f'{i + 1}- {transaction.__str__()}')
     