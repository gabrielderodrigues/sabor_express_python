from models.assessment import Assessment
from models.menu.item_menu import ItemMenu

class Restaurant:
    restaurants = []
    
    def __init__(self, name, category):
        self._name = name.title()
        self.category = category.upper()
        self._active = False
        self._assessment = []
        self._menu = []
        Restaurant.restaurants.append(self)
        
    @classmethod
    def show_restaurants(cls):
        header = f'{"Nome do Restaurante".ljust(25)} | {"Categoria".ljust(25)} | {"Avaliação".ljust(25)} | {"Status"}'
        print(header)
        print('-' * len(header))
        for restaurant in cls.restaurants:                
            print(f'{restaurant._name.ljust(25)} | {restaurant.category.ljust(25)} | {str(restaurant.calculate_average_ratings).ljust(25)} | {restaurant.active}')
            
    @property
    def active(self):
        return '☑' if self._active else '☐'
    
    def alternate_state(self):
        self._active = not self._active
        
    def receive_assessment(self, customer, rate):
        if rate < 1 or rate > 5:
            print('Avaliação inválida')
            return
        self._assessment.append(Assessment(customer, rate))
        
    @property
    def calculate_average_ratings(self):
        if not self._assessment:
            return '-'
        sum_of_ratings = sum([assessment._rate for assessment in self._assessment])
        quantity_of_ratings = len(self._assessment)
        return round(sum_of_ratings / quantity_of_ratings, 1)
        
    def add_item_menu(self, item):
        if isinstance(item, ItemMenu):
            self._menu.append(item)
            
    def show_menu(self):
        if not self._menu:
            print(f'😓 Parece que o cardápio do restaurante {self._name} está vazio...')
        else:
            print(f'Cardapio do restaurante {self._name}')
            for i, item in enumerate(self._menu):
                if hasattr(item, 'description'):
                    print(f'{i + 1} - {item._name} | Preço: R$ {item._price:.2f} | Descrição: {item.description}')
                else:
                    print(f'{i + 1} - {item._name} | Preço: R$ {item._price:.2f} | Tamanho: {item.length}ml')