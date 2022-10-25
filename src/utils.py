'''
crud functions in use by the system
'''
from tabulate import tabulate
import csv
from helpers import dict_to_csv


def print_users(data_csv):
    '''print user list'''
    try:
        with open(data_csv, 'r', encoding='utf-8') as user_csv:
            user_table = list(csv.reader(user_csv))
            print(tabulate(user_table))
    except Exception as exp:
        print(f'{exp}')


def find_user(users_dict, name):
    '''finds by name and returns user data_csv'''
    try:
        for index, user in enumerate(users_dict):
            if name == user['name']:
                return index, user, True
            else:
                return None, None, False

    except Exception as exp:
        print(f'{exp}')


def add_user(users_dict, name, gender, email, phone, cpf, birth):
    '''adds a new user'''
    try:
        users_dict.append({
            'name': name,
            'gender': gender,
            'email': email,
            'phone': phone,
            'cpf': cpf,
            'birth': birth
        })

        # write to csv
        dict_to_csv(users_dict)

        # index, user, bool_value = find_user(users_dict, name)

        # success = 'O usuário foi adicionado\n'
        # fail = 'O usuário não foi adicionado\n'

        # if bool_value is True:
        #     # return 'the new user, sucess/fail message'
        #     return user, success
        # else:
        #     return None, fail
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
