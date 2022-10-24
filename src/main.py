'''
menu do sistema
'''
from utils import print_users, find_user, add_user

n1 = '[1]Imprima a lista de usuários\n'
n2 = '[2]Busque um usuário pelo nome\n'
n3 = '[3]Cadastre um novo usuário\n'
n4 = '[4]Remova um usuário\n'
n5 = '[5]Atualize um usuário\n'
bonus = '[6]Estátisticas do sistema\n'
quit_menu = '[7]Encerrar o sistema\n'
menu = f'Digite o número da ação a ser realizada:\n{n1}{n2}{n3}{n4}{n5}{bonus}{quit_menu}'

action = input(menu)

data_csv = 'src/data.csv'

while action != '7':
    if action == '1':
        print_users(data_csv)
        action = input(menu)

    elif action == '2':
        name = input('Digite o nome do usuario que deseja buscar: ')
        find_user(data_csv, name)
        action = input(menu)

    elif action == '3':
        print('Dados do novo usuário:\n')
        name = input('nome: ')
        gender = input('genero: ')
        email = input('email: ')
        phone = input('phone: ')
        cpf = input('cpf: ')
        birth = input('data de nascimento: ')

        # user, message = add_user(data_csv, name, gender, email, phone, cpf,
        #                          birth)
        add_user(data_csv, name, gender, email, phone, cpf, birth)
        action = input(menu)

    elif action == '4':
        name = input('Digite o nome do usuario que deseja remover: ')
        # user, message = remove_user(data_csv, name)
        print('remove user\n')
        action = input(menu)

    elif action == '5':
        name = input('Digite o nome do usuario que deseja atualizar: ')
        print('Digite que item deverá ser atualizado:\n')
        key_to_updated = input(
            'nome | gênero | email | telefone | cpf | nascimento: ')
        updated_value = input('\ndigite o novo valor: ')
        # user, message = remove_user(data_csv, name, key_to_updated, updated_value)
        print('updated user\n')
        action = input(menu)

    elif action == '6':
        # system_statistics(data_csv)
        print('statistics\n')
        action = input(menu)
