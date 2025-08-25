def edit_transaction(self, index, new_transaction):
    if not 0 <= index < len(self.transactions):
        print("❌ Invalid transaction number. No changes were made.")
        return False

    transaction = self.transactions[index]
    
    updated_fields = []

    if 'amount' in new_transaction and new_transaction['amount'].strip():
        old_amount = transaction.amount
        transaction.amount = new_transaction['amount'].strip()
        updated_fields.append(f"💰 Amount: {old_amount} → {transaction.amount}")

    if 'category' in new_transaction and new_transaction['category'].strip():
        old_category = transaction.category
        transaction.category = new_transaction['category'].strip()
        updated_fields.append(f"📁 Category: {old_category} → {transaction.category}")

    if 'date' in new_transaction and new_transaction['date'].strip():
        old_date = transaction.date
        transaction.date = new_transaction['date'].strip()
        updated_fields.append(f"📅 Date: {old_date} → {transaction.date}")

    if 'type' in new_transaction and new_transaction['type'].strip():
        old_type = transaction.type
        transaction.type = new_transaction['type'].strip()
        updated_fields.append(f"🔖 Type: {old_type} → {transaction.type}")

    if 'description' in new_transaction and new_transaction['description'].strip():
        old_desc = transaction.description
        transaction.description = new_transaction['description'].strip()
        updated_fields.append(f"📝 Note: '{old_desc}' → '{transaction.description}'")

    self.save_file()

    print("\n✅ Transaction updated successfully!")
    print("📌 Changes applied:")
    for field in updated_fields:
        print(f"   • {field}")

    if not updated_fields:
        print("🔸 No changes were made.")

    return True