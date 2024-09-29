import os

restaurants = [
    {'name':'Pizza', 'categoria':'Japonesa', 'ativo': False}, 
    {'name':'Burguer', 'categoria':'Fast Food', 'ativo': True}, 
    {'name':'Sushi', 'categoria':'Japonesa', 'ativo': False}
]

def show_logo():
    print("== Sabor Express ==")

def show_options():    
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
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
    print(subtitle)
    print()
    
def create_new_restaurant():
    show_subtitle('Cadastrar restaurante')
    
    name_of_restaurant = input('Digite o nome do restaurante que deseja cadastrar: ')
    restaurants.append(name_of_restaurant)
    print(f'Restaurante {name_of_restaurant} cadastrado com sucesso!\n')
    return_to_menu()
    
def show_restaurants():
    show_subtitle('Listar restaurantes')
    
    for restaurant in restaurants:
        restaurant_name = restaurant['name']
        restaurant_category = restaurant['categoria']
        
        if (restaurant['ativo']):
            restaurant_active = 'Ativo'
        else:
            restaurant_active = 'Inativo'
            
        print(f"- {restaurant_name} | {restaurant_category} | {restaurant_active}")
        
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
            print('Ativar restaurante')
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