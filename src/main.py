'''
menu do sistema
'''
from utils import print_users, find_user, add_user, remove_user, update_user, system_statistics
from csv_helpers import csv_to_dict
from data_input_helpers import ask_for_name, ask_for_gender, ask_for_email, ask_for_phone, ask_for_cpf, ask_for_birth, check_key_before_asking

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
    # print all users
    if action == '1':
        print_users(data_csv)
        action = input(menu)

    # search for a user
    elif action == '2':
        name = input('\nDigite o nome do usuario que deseja buscar: ').lower()
        users_dict = csv_to_dict(data_csv)
        users, bool_val = find_user(users_dict, name)

        if bool_val is True:
            for user in users:
                print(
                    f"{user['name']} | {user['gender']} | {user['email']} | {user['phone']} |{user['cpf']} | {user['birth']}\n"
                )
        else:
            print('Usuário não existe\n')
        action = input(menu)

    # add a new user
    elif action == '3':
        print('\nDados do novo usuário:\n')
        name, message = ask_for_name()
        while name == None:
            print(message)
            name, message = ask_for_name()
        gender, message = ask_for_gender()
        email, message = ask_for_email()
        while email == None:
            print(message)
            email, message = ask_for_email()
        phone, message = ask_for_phone()
        while phone == None:
            print(message)
            phone, message = ask_for_phone()
        cpf, message = ask_for_cpf()
        while cpf == None:
            print(message)
            cpf, message = ask_for_cpf()
        birth, message = ask_for_birth()
        while birth == None:
            print(message)
            birth, message = ask_for_birth()

        users_dict = csv_to_dict(data_csv)

        if message == True:
            bool_value, message, user = add_user(users_dict, name, gender,
                                                 email, phone, cpf, birth)

            if bool_value == False:
                print(message)
            else:
                print(message)
                print(
                    f"{user['name']} | {user['gender']} | {user['email']} | {user['cpf']} | {user['birth']}\n"
                )
        else:
            print(message)

        action = input(menu)

    # remove a user
    elif action == '4':
        name = input('\nDigite o nome do usuario que deseja remover: ').lower()

        users_dict = csv_to_dict(data_csv)
        user, message = remove_user(users_dict, name)

        if message == 'Usuário foi removido\n':
            print(message)
            print(
                f"{user['name']} | {user['gender']} | {user['email']} | {user['cpf']} | {user['birth']}\n"
            )
        else:
            print(
                'Algo deu errado. Tente novamente ou entre em contato com o suporte.\n'
            )

        action = input(menu)

    # update a user
    elif action == '5':
        name = input(
            '\nDigite o nome do usuario que deseja atualizar: ').lower()
        users_dict = csv_to_dict(data_csv)
        keys = ['nome', 'gênero', 'email', 'telefone', 'cpf', 'nascimento']

        user, bool_value = find_user(users_dict, name)

        if user != None:
            if len(user) > 1:
                print('Edição de múltiplos usuários a ser implementada\n')
            else:
                user = user[0]

                print('Digite que item deverá ser atualizado:')
                key_to_update = input(
                    f'{keys[0]} | {keys[1]} | {keys[2]} | {keys[3]} | {keys[4]} | {keys[5]}:\n'
                )

                updated_value, message = check_key_before_asking(
                    key_to_update, keys)

                if updated_value == None:
                    print(message)
                elif updated_value != None:
                    user, converted_key = update_user(users_dict, name,
                                                      key_to_update,
                                                      updated_value)

                    if user[converted_key] == updated_value:
                        print('Usuário foi alterado\n')
                        print(
                            f"{user['name']} | {user['gender']} | {user['email']} | {user['cpf']} | {user['birth']}\n"
                        )
                    else:
                        print(
                            'Algo deu errado. Tente novamente ou entre em contato com o suporte.\n'
                        )
        else:
            print('Usuário não existe\n')

        action = input(menu)

    # print system statistics
    elif action == '6':
        users_dict = csv_to_dict(data_csv)
        users_count, gender_count_dict = system_statistics(users_dict)

        print(f'Total de usuários cadastrados: {users_count}\n')

        print('Usuários por gênero:\n')
        for gender in gender_count_dict:
            print(f'{gender}: {gender_count_dict[gender]}')
        print('\n')

        action = input(menu)
