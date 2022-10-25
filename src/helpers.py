'''
helper functions in use by the system
'''
import csv


def dict_to_csv(data_dict):
    user_info = ['name', 'gender', 'email', 'phone', 'cpf', 'birth']
    try:
        with open('src/data.csv', 'w', encoding='utf-8') as data:
            writer = csv.DictWriter(data, fieldnames=user_info)
            writer.writeheader()
            writer.writerows(data_dict)
    except Exception as exp:
        print(f'{exp}')


def csv_to_dict(data_csv):
    try:
        with open(data_csv, 'r', encoding='utf-8') as data:
            dict_reader = csv.DictReader(data)
            users_dict = list(dict_reader)
            return users_dict
    except Exception as exp:
        print(f'{exp}')


def find_last_in_csv(name):
    try:
        with open('src/data.csv', 'r', encoding='utf-8') as data:
            users = data.readlines()
            if name == users[-1].split(',')[0]:
                return True
            else:
                return False
    except Exception as exp:
        print(f'{exp}')
