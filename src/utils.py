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
                print(tabulate(data_csv, headers='firstrow'))


def add_user(data_csv, name, gender, email, phone, cpf, birth):
    '''adds a new user'''
    return 'the new user, sucess/fail message'


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
