from finance.transaction_list import TransactionList


def menu():
    print("\n" + "💰 " + "━" * 40)
    print("           PERSONAL EXPENSE TRACKER")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("📌 What would you like to do?")
    print("1️⃣  Record Income")
    print("2️⃣  Record Expense")
    print("3️⃣  View All Transactions")
    print("4️⃣  Edit a Transaction")
    print("5️⃣  Delete a Transaction")
    print("6️⃣  Search Transactions")
    print("7️⃣  Filter by Time")
    print("8️⃣  Generate Report")
    print("9️⃣  Exit")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")


def get_action():
    try:
        action = int(input("\n🔢 Please select an option (1-9): "))
        if 1 <= action <= 9:
            return action
        else:
            print("❌ Please enter a number between 1 and 9.")
    except ValueError:
        print("❌ Invalid input! Please enter a number.")


def main():
    transactions = TransactionList()  # ایجاد یک نمونه از TransactionList

    try:
        while True:
            menu()
            user_choice = get_action()

            if user_choice == 1:
                print("\n🟢 Recording New Income")
                transactions.add(type='income')

            elif user_choice == 2:
                print("\n🔴 Recording New Expense")
                transactions.add(type='expense')

            elif user_choice == 3:
                print("\n📋 Viewing All Transactions")
                transactions.display()

            elif user_choice == 4:
                print("\n✏️  Edit a Transaction")
                if not transactions.transactions:
                    print("📭 No transactions available to edit.")
                    continue

                transactions.display()
                try:
                    index = int(input("\n🔢 Select transaction number to edit: ")) - 1
                    if 0 <= index < len(transactions.transactions):
                        print(f"\n🔧 Editing transaction #{index + 1}")
                        amount = input("💵 New Amount (leave empty to keep): ").strip()
                        category = input("📁 New Category (leave empty to keep): ").strip()
                        date = input("📅 New Date (YYYY-MM-DD, leave empty to keep): ").strip()
                        t_type = input("🔖 New Type (income/expense, leave empty to keep): ").strip()
                        description = input("📝 New Description (leave empty to keep): ").strip()

                        new_transaction = {
                            'amount': amount,
                            'category': category,
                            'date': date,
                            'type': t_type,
                            'description': description
                        }
                        transactions.edit(index, new_transaction)
                    else:
                        print("❌ Invalid transaction number.")
                except ValueError:
                    print("❌ Please enter a valid number.")

            elif user_choice == 5:
                print("\n🗑️  Delete a Transaction")
                if not transactions.transactions:
                    print("📭 No transactions available to delete.")
                    continue

                transactions.display()
                try:
                    index = int(input("\n🔢 Select transaction number to delete: ")) - 1
                    if 0 <= index < len(transactions.transactions):
                        transactions.remove(index)
                    else:
                        print("❌ Invalid transaction number.")
                except ValueError:
                    print("❌ Please enter a valid number.")

            elif user_choice == 6:
                print("\n🔍 Search Transactions")
                query = input("🔎 Enter search term (category, amount, description...): ").strip()
                if not query:
                    print("💡 Search term cannot be empty.")
                    continue

                result = transactions.searches(query)
                if result:
                    print(f"\n🎯 Found {len(result)} result(s):")
                    for i, item in enumerate(result, 1):
                        emoji = "🟢" if item.type == 'income' else "🔴"
                        print(f"{emoji} {i}. {item}")
                else:
                    print("📭 No matching transactions found.")

            elif user_choice == 7:
                print("\n📅 Filter Transactions by Time")
                print("1️⃣  Today")
                print("2️⃣  This Week")
                print("3️⃣  This Month")
                print("4️⃣  Custom Range")

                try:
                    filter_type = int(input("\n🔢 Choose filter type (1-4): "))
                except ValueError:
                    print("❌ Please enter a valid number (1-4).")
                    continue

                time_frame = None
                if filter_type == 1:
                    time_frame = 'today'
                elif filter_type == 2:
                    time_frame = 'current week'
                elif filter_type == 3:
                    time_frame = 'current month'
                elif filter_type == 4:
                    time_frame = 'range'
                else:
                    print("❌ Invalid choice. Please select 1 to 4.")
                    continue

                result = transactions.filter_item(time_frame)
                if not result:
                    print("📭 No transactions found for this period.")
                else:
                    print(f"\n🎯 {len(result)} transaction(s) found:")
                    for i, item in enumerate(result, 1):
                        emoji = "🟢" if item.type == 'income' else "🔴"
                        print(f"{emoji} {i}. {item}")

            elif user_choice == 8:
                print("\n📊 Generate Financial Report")
                print("1️⃣  Today")
                print("2️⃣  This Week")
                print("3️⃣  This Month")
                print("4️⃣  Custom Range")

                try:
                    filter_type = int(input("\n🔢 Choose time frame (1-4): "))
                except ValueError:
                    print("❌ Please enter a valid number.")
                    continue

                time_frame = None
                if filter_type == 1:
                    time_frame = 'today'
                elif filter_type == 2:
                    time_frame = 'current week'
                elif filter_type == 3:
                    time_frame = 'current month'
                elif filter_type == 4:
                    time_frame = 'range'
                else:
                    print("❌ Invalid choice.")
                    continue

                category = input("🔖 Filter by category? (Press Enter for all): ").strip()
                if not category:
                    category = 'all'

                transactions.reports(time_frame, category)

            elif user_choice == 9:
                print("👋 Thank you for using Expense Tracker!")
                print("💾 Saving your data...")
                transactions.save_file()
                print("✅ Your data has been saved.")
                print("🎉 Goodbye!")
                break

    except KeyboardInterrupt:
        print("\n\n👋 Program interrupted by user (Ctrl+C).")
        print("💾 Saving your data before exit...")
        transactions.save_file()
        print("✅ Your data has been saved safely.")
        print("👋 Goodbye!")


if __name__ == '__main__':
    main()