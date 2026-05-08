class Product:

    def __init__(self, model, name, quantity):
        self.model = str(model)
        self.name = str(name)
        self.quantity = int(quantity)

    def update_stock(self, amount):
        amount = int(amount)
        if self.quantity + amount < 0:
            raise ValueError("Stock cannot go below zero")
        self.quantity += amount

    def to_dict(self):
        return {
            "model": self.model,
            "name": self.name,
            "quantity": self.quantity
        }