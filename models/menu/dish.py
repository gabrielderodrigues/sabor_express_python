from models.menu.item_menu import ItemMenu

class Dish(ItemMenu):
    def __init__(self, name, price, description):
        super().__init__(name, price)
        self.description = description