import datetime

def insert_transaction(self, class_name, type):
        amount = input('Amount : ')
        category = input('Category : ')
        date = datetime.date.today()
        type = type
        description = input('Description : ')
        data = class_name(amount, category, date, description, type)
        self.transactions.append(data)
        self.save_file()
        print('\nSuccessfully')
        return True
    