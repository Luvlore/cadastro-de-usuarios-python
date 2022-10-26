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

    birth_list = birth.split('/')
    day = int(birth_list[0])
    month = int(birth_list[1])
    year = int(birth_list[2])

    date_birth = datetime.date(year, month, day)
    date_today = datetime.date.today()

    if len(birth) < 8 or len(birth.split('/')) == 1:
        message = 'Formato Incorreto. Por favor escreva a data neste formato: dd/mm/aaaa\n'
        return None, message
    elif date_birth > date_today:
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
