import datetime

def insert_transaction(self, class_name, type):
    print(f"\n📝 Adding New {type.capitalize()}")

    while True:
        try:
            amount_input = input("💰 Amount (e.g., 500000): ").strip()
            amount = float(amount_input)
            if amount <= 0:
                print("❌ Amount must be greater than zero. Please try again.")
                continue
            break
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")

    category = input("📁 Category (e.g., Food, Salary): ").strip()
    while not category:
        print("❌ Category cannot be empty.")
        category = input("📁 Category: ").strip()

    description = input("📘 Description (optional, press Enter to skip): ").strip()
    if not description:
        description = "No description"

    date = datetime.date.today()

    transaction = class_name(amount, category, str(date), description, type)
    self.transactions.append(transaction)
    self.save_file()

    print(f"\n✅ {type.capitalize()} successfully added!")
    print(f"📥 {amount:,} Toman | {category} | {date}")
    if description != "No description":
        print(f"📌 Note: {description}")

    return True