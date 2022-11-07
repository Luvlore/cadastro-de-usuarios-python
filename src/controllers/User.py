import csv

from prettytable import PrettyTable
from utils.clear_screen import clear_screen
from utils.finders import find_id, menu_find
from utils.validations import *
from utils.verify_age import verify_age

field_names_table = ['ID', 'Nome', 'Gênero', 'Email', 'Telefone', 'CPF', 'Data de Nascimento']

def find_all():
  clear_screen()
  try:
    with open('src/database/users.csv', 'r') as file:
      users = csv.DictReader(file)

      table = PrettyTable()
      table.title = 'TODOS USUÁRIOS LISTADOS'
      table.field_names = field_names_table

      for pos, user in enumerate(users):
        table.add_row([pos, *user.values()])

      print(table)

      input('Aperte Enter tecla para continuar: ')
      pass
  except Exception:
    print('Erro no arquivo')

def find_by_name():
  clear_screen()

  try:
    with open('src/database/users.csv', 'r') as file:
      name = input('Digite o nome: ')

      users = csv.DictReader(file)

      table = PrettyTable()
      table.title = f'RESULTADOS PARA {name.upper()}'
      table.field_names = field_names_table

      users_found = [[pos, *user.values()] for pos, user in enumerate(users) if name.lower() in user['name'].lower()]

      for user in users_found:
        table.add_row(user)

      clear_screen()

      print(table)
      input('Aperte Enter para continuar: ')

      pass
  except Exception:
    print('Erro no arquivo')

def create(id=False, user_update=False):
  new_user = {
    'name': user_update.split(',')[0] if user_update else '',
    'gender': user_update.split(',')[1] if user_update else '',
    'email': user_update.split(',')[2] if user_update else '',
    'phone': user_update.split(',')[3] if user_update else '',
    'cpf': user_update.split(',')[4] if user_update else '',
    'birthdate': user_update.split(',')[5] if user_update else ''
  }

  fields_functions = {
    'name': {'title': 'o nome', 'func': validate_name},
    'gender': {'title': 'o gênero', 'func': validate_gender},
    'email': {'title': 'o email', 'func': validate_email},
    'cpf': {'title': 'o CPF', 'func': validate_cpf},
    'phone': {'title': 'o telefone', 'func': validate_phone},
    'birthdate': {'title': 'a data de nascimento', 'func': validate_birthdate},
  }

  while True:
    clear_screen()

    print(f'{"ATUALIZAÇÃO" if user_update else "CRIAÇÃO"} DE NOVO USUÁRIO')

    for pos, (opKey, op) in enumerate(fields_functions.items()):
      if user_update:
        change = ' '

        while change not in 'SN':
          change = input(f'Deseja mudar {op["title"]}? [S/N] ').strip().upper()[0]

        if change == 'S':
          new_user[opKey] = op['func']()
      else:
        new_user[opKey] = op['func']()


    clear_screen()

    table = PrettyTable()
    table.title = f'USUÁRIO {"ATUALIZADO" if user_update else "CRIADO"}'
    table.field_names = field_names_table[1:]
    table.add_row(new_user.values())

    print(table)

    resp = ' '

    while resp not in 'SN':
      resp = input('As informações conferem? ').strip().upper()[0]

    if resp == 'S':
      if user_update:
        list_updated = []

        with open('src/database/users.csv', 'r') as file:
          users = file.readlines()

          for pos, user in enumerate(users):
            if id == pos - 1:
              print(id)
              updated = f"{','.join(list(new_user.values()))}\n"
              list_updated.append(updated)
            else:
              list_updated.append(user)
          pass

        with open('src/database/users.csv', 'w') as file:
          for user in list_updated:
            file.write(user)
          pass
        break
      else:
        with open('src/database/users.csv', 'a') as file:
          fieldnames = new_user.keys()
          writer = csv.DictWriter(file, fieldnames)

          writer.writerow(new_user)

          pass
        break

find_user = {
  'Ver lista de todos os usuário': find_all,
  'Encontrar usuário pelo nome': find_by_name
}

def delete():
  menu_find(find_user)
  list_updated = []
  user_deleted = ''

  while True:
    with open('src/database/users.csv', 'r') as file:
      users = file.readlines()

      try:
        user_to_delete = find_id(users)

        for pos, user in enumerate(users):
          if int(user_to_delete) != pos - 1:
            list_updated.append(user)
          else:
            user_deleted = user.split(',')[0]
        pass

        with open('src/database/users.csv', 'w') as file:
          for user in list_updated:
            file.write(user)
          pass

        input(f'USUÁRIO {user_deleted.upper()} FOI REMOVIDO COM SUCESSO!')

        break
      except Exception as err:
        print(err)

      pass

def update():
  menu_find(find_user)

  while True:
   with open('src/database/users.csv', 'r') as file:
    try:
      users = file.readlines()
      id = find_id(users)

      create(id, users[id + 1])

      break
    except Exception as err:
      print(err)

def statistics():
  with open('src/database/users.csv', 'r') as file:
    all_users = list(csv.DictReader(file))

    statistics_dict = {
      'all': {
        'title': 'Todos os usuários',
        'quantity': len(all_users)
      },
      'females': {
        'title': 'Mulheres',
        'quantity': len([user for user in all_users if user['gender'] == 'feminino'])
      },
      'males': {
        'title': 'Homens',
        'quantity': len([user for user in all_users if user['gender'] == 'masculino'])
      },
      'others': {
        'title': 'Outros',
        'quantity': len([user for user in all_users if user['gender'] == 'outro'])
      },
      'minors': {
        'title': 'Menores de 18 anos',
        'quantity': len([user for user in all_users if verify_age(user['birthdate']) == 'minor'])
      },
      'youngs': {
        'title': 'Entre 18 anos a 35 anos',
        'quantity': len([user for user in all_users if verify_age(user['birthdate']) == 'young'])
      },
      'majors': {
        'title': 'Entre 35 anos a 65 anos',
        'quantity': len([user for user in all_users if verify_age(user['birthdate']) == 'major'])
      },
      'elders': {
        'title': 'Maiores que 65 anos',
        'quantity': len([user for user in all_users if verify_age(user['birthdate']) == 'elder'])
      },
    }

    table = PrettyTable()
    table.title = 'ESTATÍSTICAS DOS USUÁRIOS'
    table.field_names = ['Tipo', 'Quantidade']

    for statistic in statistics_dict.values():
      table.add_row([statistic['title'], statistic['quantity']])

    clear_screen()
    print(table)
    input()
    pass
