'''
crud functions in use by the system
'''
from tabulate import tabulate
import csv
from csv_helpers import dict_to_csv, find_last_in_csv, csv_to_dict
from collections import Counter
from data_input_helpers import get_ages, count_ages


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
            if name == user['name']:
                user_exists.append(user)

        if len(user_exists) == 0:
            return None, False
        elif len(user_exists) > 0:
            return user_exists, True
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
            if len(user) > 1:
                print('Remoção de múltiplos usuários a ser implementada')
                return None, fail
            else:
                user = user[0]

                users_dict.remove(user)
                dict_to_csv(users_dict)

            return user, success

    except Exception as exp:
        print(f'{exp}')


def update_user(users_dict, name, key_to_update, updated_value):
    '''find by name and updates user'''
    # could find by other keys
    try:
        convert_key = {
            'nome': 'name',
            'gênero': 'gender',
            'email': 'gender',
            'telefone': 'phone',
            'cpf': 'cpf',
            'nascimento': 'birth'
        }

        if key_to_update in convert_key:
            for index, user in enumerate(users_dict):
                if user['name'] == name:
                    user[convert_key[key_to_update]] = updated_value
                    user_index = index

            dict_to_csv(users_dict)
            csv = 'src/data.csv'
            updated_users_dict = csv_to_dict(csv)

            return updated_users_dict[user_index], convert_key[key_to_update]
        else:
            return None

    except Exception as exp:
        print(f'{exp}')
    # return 'the updated user(before/after), sucess/fail message'


def system_statistics(users_dict):
    '''prints a formatted text of the system's statistics'''
    # get users total
    users_count = len(users_dict)

    # get genders
    gender = []
    for user in users_dict:
        gender.append(user['gender'])

    gender_count_dict = Counter(gender)

    # get ages
    ages = get_ages(users_dict)
    count_ages(ages)

    return users_count, gender_count_dict
