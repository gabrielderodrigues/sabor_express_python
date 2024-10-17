class ItemMenu:
    def __init__(self, name, price):
        self._name = name
        self._price = price

    def __str__(self):
        return f"{self.name} - ${self.price:.2f}"