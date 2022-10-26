'''
helper functions in use by the system
'''
import csv
import re
import phonenumbers


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


def ask_for_name():
    name = input('nome: ').lower()
    if len(name) < 2:
        message = 'Nome inválido\n'
        return None, message

    return name, True


def ask_for_gender():
    gender = input('genero: ').lower()
    return gender, True


def ask_for_email():
    email = input('email: ').lower()
    regex_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if not re.fullmatch(regex_email, email):
        message = 'Email inválido\n'
        return None, message

    return email, True


def ask_for_phone():
    phone = input('telefone(somente números): ')
    my_number = phonenumbers.parse(phone, 'BR')
    if not phonenumbers.is_valid_number(my_number):
        message = 'Telefone inválido\n'
        return None, message

    return phone, True


def ask_for_cpf():
    cpf = input('cpf: ')
    if len(cpf) != 11:
        message = 'Cpf inválido\n'
        return None, message

    return cpf, True


def ask_for_birth():
    birth = input('data de nascimento(dd/mm/aaaa): ')
    if len(birth) < 8 or len(birth.split('/')) == 1:
        message = 'Por favor escreva a data neste formato: dd/mm/aaaa\n'
        return None, message

    return birth, True
