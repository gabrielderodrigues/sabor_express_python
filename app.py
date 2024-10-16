import os

from models.restaurant import Restaurant

restaurants = [
    Restaurant('Praça São Lourenço', 'Brasileira'),
    Restaurant('Madero', 'Hamburgueria'),
    Restaurant('Montana', 'Churrascaria')
]

def show_logo():
    print("== Sabor Express ==")

def show_options():    
    print('1. Cadastrar restaurantes')
    print('2. Listar restaurantes')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n')
    
def exit_app():
    show_subtitle('Até mais.')
    
def return_to_menu():
    input('\nDigite uma tecla para voltar para o menu...')
    main()
    
def invalid_option():
    print('Opção inválida\n')
    return_to_menu()
    
def show_subtitle(subtitle):
    os.system('cls')
    line = '*' * (len(subtitle))
    print(line)
    print(subtitle)
    print(line)
    print()
    
def create_new_restaurant():
    show_subtitle('Cadastrar restaurante')
    
    name_of_restaurant = input('Digite o nome do restaurante que deseja cadastrar: ')
    category_of_restaurant = input('Digite a categoria do restaurante: ')
    
    restaurants.append(
        Restaurant(name_of_restaurant, category_of_restaurant)
    )
    
    print(f'Restaurante {name_of_restaurant} cadastrado com sucesso!\n')
    return_to_menu()
    
def show_restaurants():
    show_subtitle('Listar restaurantes')
    
    Restaurant.show_restaurants()
        
    return_to_menu()
    
def change_restaurant_status():
    show_subtitle('Alternando estado do restaurante...')
    
    restaurant_name = input('Digite o nome do restaurante que deseja ativar/inativar: ')
    
    restaurant_found = False
    
    for restaurant in restaurants:
        if restaurant._name == restaurant_name:
            restaurant_found = True
            restaurant.alternate_state()
            message = f'O restaurante {restaurant_name} foi ativado com sucesso!' if restaurant._active else f'O restaurante {restaurant_name} foi inativado com sucesso!'
            print(message)
            break
    
    if not restaurant_found:
        print('Restaurante não encontrado.')
    
    return_to_menu()

def choose_option():
    try:
        choosed_option = int(input('Digite uma opção: '))
    except ValueError:
        print('Opção inválida')
        exit()
        
    match choosed_option:
        case 1:
            create_new_restaurant()
        case 2:
            show_restaurants()
        case 3:
            change_restaurant_status()
        case 4:
            exit_app()
        case _:
            invalid_option()
    
def main():
    show_logo()
    show_options()
    choose_option()
    
if __name__ == '__main__':
    main()