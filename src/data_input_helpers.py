'''
data input helper functions in use by the system
'''
import re
import phonenumbers
import datetime


def ask_for_name():
    name = input('\nDigite o nome: ').lower()
    if len(name) < 2:
        message = 'Nome inválido\n'
        return None, message

    return name, True


def ask_for_gender():
    gender = input('\nDigite o gênero: ').lower()
    return gender, True


def ask_for_email():
    email = input('\nDigite um email válido: ').lower()
    regex_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if not re.fullmatch(regex_email, email):
        message = 'Email inválido\n'
        return None, message

    return email, True


def ask_for_phone():
    phone = input('\nDigite o telefone(somente números): ')
    try:
        my_number = phonenumbers.parse(phone, 'BR')

        if not phonenumbers.is_valid_number(my_number):
            message = 'Telefone inválido\n'
            return None, message
    except Exception:
        message = 'Telefone inválido\n'
        return None, message

    return phone, True


def ask_for_cpf():
    cpf = input('\nDigite o cpf(somente números): ')
    if len(cpf) != 11:
        message = 'Cpf inválido\n'
        return None, message

    return cpf, True


def ask_for_birth():
    birth = input('\ndata de nascimento(dd/mm/aaaa): ')

    if len(birth) < 8 or len(birth.split('/')) == 1:
        message = 'Formato Incorreto. Por favor escreva a data neste formato: dd/mm/aaaa\n'
        return None, message

    birth_list = birth.split('/')
    day = int(birth_list[0])
    month = int(birth_list[1])
    year = int(birth_list[2])

    if month > 12:
        message = 'Por favor digite um mês válido.\n'
        return None, message

    date_birth = datetime.date(year, month, day)
    date_today = datetime.date.today()

    if date_birth > date_today:
        message = 'Por favor digite uma data anterior à atual.\n'
        return None, message
    elif year < 1894:
        message = 'Por favor digite uma data apòs 1894.\n'
        return None, message
    return birth, True


def check_key_before_asking(key_to_update, keys):
    if key_to_update in keys:
        if key_to_update == 'nome':
            updated_value, message = ask_for_name()
            if updated_value is None:
                return None, message
        elif key_to_update == 'gênero':
            updated_value, message = ask_for_gender()
            if updated_value is None:
                return None, message
        elif key_to_update == 'email':
            updated_value, message = ask_for_email()
            if updated_value is None:
                return None, message
        elif key_to_update == 'telefone':
            updated_value, message = ask_for_phone()
            if updated_value is None:
                return None, message
        elif key_to_update == 'cpf':
            updated_value, message = ask_for_cpf()
            if updated_value is None:
                return None, message
        elif key_to_update == 'nascimento':
            updated_value, message = ask_for_birth()
            if updated_value is None:
                return None, message
    else:
        return None, '\nItem não existe, ou foi digitado incorretamente.\n'

    return updated_value, message


def get_ages(users_dict):
    ages = []
    date_today = datetime.date.today()

    for user in users_dict:
        birth_list = user['birth'].split('/')
        day = int(birth_list[0])
        month = int(birth_list[1])
        year = int(birth_list[2])

        date_birth = datetime.date(year, month, day)
        age = date_today.year - date_birth.year - (
            (date_today.month, date_today.day) <
            (date_birth.month, date_birth.day))

        ages.append(age)

    return ages


def count_ages(ages):
    # up to 18
    group_1 = []
    # 18 - 35
    group_2 = []
    # 35 - 65
    group_3 = []
    # over 65
    group_4 = []

    for age in ages:
        if age < 18:
            group_1.append(age)
        elif age > 18 and age < 35:
            group_2.append(age)
        elif age > 35 and age < 65:
            group_3.append(age)
        else:
            group_4.append(age)

    return group_1, group_2, group_3, group_4
