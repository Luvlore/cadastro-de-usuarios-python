'''
crud functions in use by the system
'''
from tabulate import tabulate
import csv
from helpers import dict_to_csv, find_last_in_csv


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
        user_exists = []

        for user in users_dict:
            if name in user['name']:
                user_exists.append(user)

        if len(user_exists) == 0:
            return None, False
        elif len(user_exists) == 1:
            return user_exists[0], True
        # elif len(user_exists) > 1:
        # how to return for multiple found users?

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

        success = 'O usuário foi adicionado\n'
        fail = 'O usuário não foi adicionado\n'
        added_user = users_dict[-1]

        if find_last_in_csv(name) is True:
            # return 'the new user, sucess/fail message'
            return True, success, added_user
        else:
            return False, fail, None
    except Exception as exp:
        print(f'{exp}')


def remove_user(users_dict, name):
    '''find by name and removes user'''
    # could find by other keys
    try:
        user, bool_value = find_user(users_dict, name)
        fail = 'Usuário não existe\n'
        success = 'Usuário foi removido\n'

        if bool_value is False:
            return None, fail
        else:
            users_dict.remove(user)
            dict_to_csv(users_dict)

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
