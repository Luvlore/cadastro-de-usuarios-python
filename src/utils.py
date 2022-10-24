'''
functions in use by the system
'''


def print_users(data):
    '''print user list'''
    with open(data, 'r', encoding='utf-8') as user_csv:
        users = user_csv.readlines()
        for user in users:
            print(user)
    return 'user list'


def find_user(data, name):
    '''finds by name and returns user data'''
    return 'user data'


def add_user(data, name, gender, email, phone, cpf, birth):
    '''adds a new user'''
    return 'the new user, sucess/fail message'


def remove_user(data, name):
    '''find by name and removes user'''
    # could find by other keys
    return 'the new user, sucess/fail message'


def atualiza_user(data, name, key_to_updated, updated_value):
    '''find by name and updates user'''
    # could find by other keys
    return 'the updated user(before/after), sucess/fail message'


def system_statistics(data):
    '''prints a formatted text of the system's statistics'''
    return 'statistics'
