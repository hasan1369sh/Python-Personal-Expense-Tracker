def remove_transaction(self, index):
    if not 0 <= index < len(self.transactions):  
        print("❌ Invalid transaction number. Nothing was removed.")
        return False

    removed_transaction = self.transactions.pop(index)
    self.save_file()

    print("\n🗑️ Transaction successfully removed!")
    print(f"   • 💰 {removed_transaction.amount:,} Toman")
    print(f"   • 📁 {removed_transaction.category}")
    print(f"   • 📅 {removed_transaction.date}")
    print(f"   • 🔖 {removed_transaction.type.capitalize()}")
    if removed_transaction.description and removed_transaction.description.lower() != "no description":
        print(f"   • 📝 Note: {removed_transaction.description}")

    return True