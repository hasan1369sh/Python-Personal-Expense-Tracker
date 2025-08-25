def diplay_transactions(self):
    print("\n📋 Transaction List")
    print("—" * 60)

    if len(self.transactions) == 0:
        print("📭 Your transaction list is empty.")
        print("💡 You can add income or expenses to get started.")
    else:
        for i, transaction in enumerate(self.transactions, 1):
            if transaction.type == "income":
                icon = "🟢"
                label = "INCOME"
            elif transaction.type == "expense":
                icon = "🔴"
                label = "EXPENSE"
            else:
                icon = "🔵"
                label = "OTHER"

            print(f"{icon} {i}. {label}")
            print(f"   💰 Amount: {transaction.amount:,} Toman")
            print(f"   📁 Category: {transaction.category}")
            print(f"   📅 Date: {transaction.date}")
            if transaction.description and transaction.description.lower() != "no description":
                print(f"   📝 Note: {transaction.description}")
            print("—" * 60)

    print()  