'''
functions in use by the system
'''
from tabulate import tabulate
import csv


def print_users(data_csv):
    '''print user list'''
    try:
        with open(data_csv, 'r', encoding='utf-8') as user_csv:
            user_table = list(csv.reader(user_csv))
            print(tabulate(user_table))
    except Exception as exp:
        print(f'{exp}')


def find_user(data_csv, name):
    '''finds by name and returns user data_csv'''
    try:
        with open(data_csv, 'r', encoding='utf-8') as user_csv:
            users = user_csv.readlines()
            found_user = []

            for user in users:
                user_list = user.split(',')
                if name in user_list:
                    found_user.append(user_list)

            if len(found_user) > 0:
                return True, found_user[0]
            else:
                return False, None
    except Exception as exp:
        print(f'{exp}')


def add_user(data_csv, name, gender, email, phone, cpf, birth):
    '''adds a new user'''
    try:
        with open(data_csv, 'a+', encoding='utf-8') as user_csv:
            user_csv.write(
                f'{name}, {gender}, {email}, {phone}, {cpf}, {birth}\n')

        bool_value, user = find_user(data_csv, name)

        success = 'O usuário foi adicionado\n'
        fail = 'O usuário não foi adicionado\n'

        if bool_value is True:
            # return 'the new user, sucess/fail message'
            return user, success
        else:
            return None, fail
    except Exception as exp:
        print(f'{exp}')


def remove_user(data_csv, name):
    '''find by name and removes user'''
    # could find by other keys
    try:
        bool_value, user = find_user(data_csv, name)
        fail = 'Usuário não existe\n'
        success = 'Usuário foi removido\n'

        if bool_value is False:
            return None, fail
        else:
            with open(data_csv, 'r+', encoding='utf-8') as data_csv_in:

                users_list = data_csv_in.readlines()

                for user in users_list:
                    user_list = user.split(',')
                    if name in user_list:
                        index = users_list.index(user)
                        del users_list[index]
                        users_list.insert(
                            0,
                            'nome, gênero, email, telefone, cpf, data de nascimento\n'
                        )

            data_csv_new = open(data_csv, 'w', encoding='utf-8')

            for user in users_list:
                data_csv_new.write(user)

            data_csv_new.close()

            return user, success

    except Exception as exp:
        print(f'{exp}')


def atualiza_user(data_csv, name, key_to_updated, updated_value):
    '''find by name and updates user'''
    # could find by other keys
    return 'the updated user(before/after), sucess/fail message'


def system_statistics(data_csv):
    '''prints a formatted text of the system's statistics'''
    return 'statistics'


def dict_to_csv(data_csv, data_dict):
    return


def csv_to_dict(data_csv, data_dict):
    data_users = {'users': []}

    with open(data_csv, 'r') as users:
        reader = csv.reader(users)
        data_users['users'] = [{rows[0]: rows[1] for rows in reader}]

    print(data_users)
