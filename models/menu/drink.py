from models.menu.item_menu import ItemMenu

class Drink(ItemMenu):
    def __init__(self, name, price, length):
        super().__init__(name, price)
        self.length = length
        
    def apply_discount(self):
        self._price -= (self._price * 0.08)