def search_result(self, query):
    query = query.lower().strip()
    if not query:
        return []
    result = []
    for transaction in self.transactions:
        if (query in transaction.amount.lower() or
            query in transaction.category.lower() or
            query in transaction.date.lower() or
            query in transaction.type.lower() or
            query in transaction.description.lower()):
                result.append(transaction)
    return result