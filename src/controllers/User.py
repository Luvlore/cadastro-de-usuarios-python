import csv


def find_all():
  with open('src/database/users.csv', 'r') as file:
    users = file.readlines()[1:]
    
    for user in users:
      print(user)
    
    pass

def find_users_by_name(name):
  with open('src/database/users.csv', 'r') as file:
    users = csv.DictReader(file)
    
    print('USUÁRIOS ENCONTRADOS\n')
    for user in users:
      if name.lower() in user['name'].lower():
        print(
          f'Nome: {user["name"]}\n' \
          f'Gênero: {user["gender"]}\n' \
          f'Email: {user["email"]}\n' \
          f'Telefone: {user["phone"]}\n'\
          f'CPF: {user["cpf"]}\n'\
          f'Data de Nascimento: {user["birthdate"]}\n'\
        )
