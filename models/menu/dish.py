from models.menu.item_menu import ItemMenu

class Dish(ItemMenu):
    def __init__(self, name, price, description):
        super().__init__(name, price)
        self.description = description
        
    def __str__(self):
        return self._name

    def apply_discount(self):
        self._price -= (self._price * 0.08)