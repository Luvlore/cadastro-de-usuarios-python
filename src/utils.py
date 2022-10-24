'''
functions in use by the system
'''
from tabulate import tabulate
import csv


def print_users(data_csv):
    '''print user list'''
    with open(data_csv, 'r', encoding='utf-8') as user_csv:
        user_table = list(csv.reader(user_csv))
        print(tabulate(user_table))


def find_user(data_csv, name):
    '''finds by name and returns user data_csv'''
    with open(data_csv, 'r', encoding='utf-8') as user_csv:
        users = user_csv.readlines()

        for user in users:
            user_list = user.split(',')
            if name in user_list:
                print(user)

                return True, user


def add_user(data_csv, name, gender, email, phone, cpf, birth):
    '''adds a new user'''
    with open(data_csv, 'a+', encoding='utf-8') as user_csv:
        user_csv.write(f'{name}, {gender}, {email}, {phone}, {cpf}, {birth}\n')

    bool_value, user = find_user(data_csv, name)
    if bool_value is True:
        # return 'the new user, sucess/fail message'
        return user


def remove_user(data_csv, name):
    '''find by name and removes user'''
    # could find by other keys
    return 'the new user, sucess/fail message'


def atualiza_user(data_csv, name, key_to_updated, updated_value):
    '''find by name and updates user'''
    # could find by other keys
    return 'the updated user(before/after), sucess/fail message'


def system_statistics(data_csv):
    '''prints a formatted text of the system's statistics'''
    return 'statistics'
