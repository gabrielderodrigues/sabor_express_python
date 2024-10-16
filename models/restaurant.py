class Restaurant:
    restaurants = []
    
    def __init__(self, name, category):
        self._name = name.title()
        self.category = category.upper()
        self._active = False
        Restaurant.restaurants.append(self)
        
    @classmethod
    def show_restaurants(cls):
        header = f'{"Nome do Restaurante".ljust(25)} | {"Categoria".ljust(25)} | {"Status"}'
        print(header)
        print('-' * len(header))
        for restaurant in cls.restaurants:                
            print(f'{restaurant._name.ljust(25)} | {restaurant.category.ljust(25)} | {restaurant.active}')
            
    @property
    def active(self):
        return '☑' if self._active else '☐'
    
    def alternate_state(self):
        self._active = not self._active
    
restaurant_praca = Restaurant('Praça São Lourenço', 'Brasileira')
restaurant_praca.alternate_state()
restaurant_madero = Restaurant('Madero', 'Hamburgueria')
restaurant_montana = Restaurant('Montana', 'Churrascaria')
restaurant_montana.alternate_state()

Restaurant.show_restaurants()