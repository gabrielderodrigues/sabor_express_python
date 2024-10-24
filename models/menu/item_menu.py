from abc import abstractmethod

class ItemMenu:
    def __init__(self, name, price):
        self._name = name
        self._price = price

    def __str__(self):
        return f"{self._name} - ${self._price:.2f}"
    
    @abstractmethod
    def apply_discount(self, discount):
        pass