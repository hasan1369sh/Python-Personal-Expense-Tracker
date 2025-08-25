from finance.transaction import TransactionList
def menu():
    print('_____ MENU _____')
    print('\n1. Record Income')
    print('\n2. Record Expense')
    print('\n3. View Transaction List')
    print('\n4. Edit Transaction')
    print('\n5. Delete Transaction')
    print('\n6. Search')
    print('\n7. Filter')
    print('\n8. Reporting')
    print('\n9. Exit')
    
def get_action():
    try:
        action = int(input('\nPlease select the operation you want (1-9) :'))
        if 1 <= action <=9:
            return action
        else:
            print('Pleas insert a valid number beetween 1 and 9')
    except ValueError:
        print('insert a valid number')
    

def main():
    try:
        while True:
            menu()
            user_choice = get_action()
            transactions = TransactionList()
            if user_choice == 1:
                transactions.add(type='income')
            if user_choice == 2:
                transactions.add(type='expense')
            elif user_choice == 3:
                transactions.display()
            elif user_choice == 4:
                transactions.display()
                try:
                    index = int(input('Select your transaction :')) -1
                    if 0 <= index <= len(transactions.transactions):
                        amount = input('New Amount : ')
                        category = input('New Category : ')
                        date = input('New Date : ')
                        type = input('New Type (income or expense) : ')
                        description = input('New Description : ')
                        new_transaction = {
                            'amount': amount,
                            'category': category,
                            'date': date,
                            'description': description,
                            'type': type
                        }
                        transactions.edit(index, new_transaction)
                    else:
                        print('\nNotFound')
                except ValueError:
                    print('\nInsert a valid number')
            elif user_choice ==5:
                transactions.display()
                try:
                    index = int(input('Select your transaction :')) -1
                    if 0 <= index <= len(transactions.transactions):
                        transactions.remove(index)
                    else:
                        print('\nNotFound')
                except ValueError:
                    print('\nInsert a valid number')
            elif user_choice == 6:
                result = []
                query = input('\nSearch text...\n')
                if query.strip() != '':
                    result = transactions.searches(query)
                else:
                    print('\nInsert current value ...')
                    return []
                for i, item in enumerate(result):
                    print(f"{i + 1}. {item}")
            elif user_choice == 7:
                result = []
                time_frame = ''
                print('\nFilter based on : ')
                print('1. Today')
                print('2. This week')
                print('3. This month')
                print('4. Specific time')

                try:
                    filter_type = int(input('\nSpecify the filter type (1 - 4): '))
                except ValueError:
                    print("\n❌ Please enter a valid number (1-4).")
                    continue  

                if filter_type == 1:
                    time_frame = 'today'
                elif filter_type == 2:
                    time_frame = 'current week'  
                elif filter_type == 3:
                    time_frame = 'current month'
                elif filter_type == 4:
                    time_frame = 'range'
                else:
                    print('\n❌ Please insert a valid value (1-4)')
                    continue  
                result = transactions.filter_item(time_frame)
                if result is None:
                    print("⚠️  Filter returned None.")
                    result = []

                if not result:
                    print("📭 No transactions found.")
                else:
                    for i, item in enumerate(result):
                        print(f"{i + 1}. {item}")
            elif user_choice == 8:
                result = []
                time_frame = ''
                print('\nFilter based on : ')
                print('1. Today')
                print('2. This week')
                print('3. This month')
                print('4. Specific time')

                try:
                    filter_type = int(input('\nSpecify the filter type (1 - 4): '))
                except ValueError:
                    print("\n❌ Please enter a valid number (1-4).")
                    continue  
                category = input('\nIf you have a specific category in mind, enter it, otherwise press enter :')
                if category.strip() == '':
                    category = 'all'
                if filter_type == 1:
                    time_frame = 'today'
                elif filter_type == 2:
                    time_frame = 'current week'  
                elif filter_type == 3:
                    time_frame = 'current month'
                elif filter_type == 4:
                    time_frame = 'range'
                else:
                    print('\n❌ Please insert a valid value (1-4)')
                    continue  
                transactions.reports(time_frame, category)
            elif user_choice == 9:
                print("👋 Goodbye!")
                break
    except KeyboardInterrupt:
        print("\n\n👋 Program interrupted by user (Ctrl+C).")
        print("💾 Saving your contacts before exit...")
        transactions.save_file()
        print("✅ Your data has been saved safely.")
        print("👋 Goodbye!")
        
        
        
if __name__ == '__main__':
    main()
