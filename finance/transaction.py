class Transaction():
    def __init__(self, amount, category, date, description, type):
        self.amount = amount
        self.category = category
        self.date = date
        self.description = description
        self.type = type
    
    def __str__(self):
        return f"{self.category} : {self.amount} - {self.type} - {self.date} - {self.description}"
    
    def __repr__(self):
        return f"Transaction(category={self.category}, amount={self.amount}, date={self.date}, type={self.type}, description={self.description})"
    
    def to_dict(self):
        return {
            'amount': self.amount,
            'category': self.category,
            'date': self.date,
            'description': self.description,
            'type': self.type
        }
        
    @staticmethod
    def from_dict(data):
        return Transaction(data['amount'], data['category'], data['date'], data['description'], data['type'])
