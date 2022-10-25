import csv

from prettytable import PrettyTable
from utils.clear_screen import clear_screen
from utils.formatter import formatter
from utils.validations import (validate_birthdate, validate_cpf,
                               validate_email, validate_gender, validate_name,
                               validate_phone)

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
    print('Erro nor arquivo')

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
      
      print(len(users_found))
      
      for user in users_found:
        table.add_row(user)
          
      print(table)
      input('Aperte Enter para continuar: ')
      
      pass
  except Exception:
    print('Erro no aqruivo')

def menu_find():
  find_user = {
    'Ver lista de todos os usuário': find_all,
    'Encontrar usuário pelo nome': find_by_name
  }
  
  for pos, op in enumerate(find_user.keys()):    
    print(f'{pos + 1}: {op}')

  choice = input('O que deseja fazer? ')
  
  if int(choice) in list(range(1, len(find_user) + 1)):
    for pos, op in enumerate(find_user.values()):
      if pos + 1 == int(choice):
        op()

def create(id=False):
  new_user = {'name': '', 'gender': '', 'email': '', 'phone': '', 'cpf': '', 'birthdate': ''}
  while True:
    clear_screen()
    
    print(f'{"ATUALIZAÇÃO" if id else "CRIAÇÃO"} DE NOVO USUÁRIO')
    
    fields_functions = {
      'name': validate_name,
      'genders': validate_gender,
      'email': validate_email,
      'phone': validate_phone,
      'birthdate': validate_birthdate,
    }
    
    for pos, (nameOp, func) in enumerate(fields_functions.items()):
      new_user[nameOp] = func()
    
    clear_screen()
    
    table = PrettyTable()
    table.title = f'USUÁRIO {"ATUALIZADO" if id else "CRIADO"}'
    table.field_names = field_names_table[1:]
    table.add_row(new_user.values())
    
    print(table)
  
    resp = ' '
    
    while resp not in 'SN':
      resp = input('As informações conferem? ').strip().upper()[0]
      
    if resp == 'S':
      if id:
        list_updated = []
        
        with open('src/database/users.csv', 'r') as file:
          users = file.readlines()
        
          for pos, user in enumerate(users):
            if int(id) + 1 == pos:
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
            
def find_id(users):
  id = input('Escolha o usuário que pelo ID: ')
        
  if not id.isdigit() or int(id) not in list(range(0, len(users) - 1)):
    raise ValueError('Digite um ID válido!')

  return id

def delete():
  menu_find()
  list_updated = []
  
  while True:
    with open('src/database/users.csv', 'r') as file:
      users = file.readlines()
      try:
        user_to_delete = find_id(users)
      
        for pos, user in enumerate(users):
          if int(user_to_delete) != pos - 1:
            list_updated.append(user)
        pass
              
        with open('src/database/users.csv', 'w') as file:
          for user in list_updated:
            file.write(user)
          pass
        break
        
      except Exception as err:
        print(err)
        
      pass

def update():
  menu_find()
  
  while True:
   with open('src/database/users.csv', 'r') as file:
    try:
      users = file.readlines()
      user_to_update = find_id(users)
     
      create(user_to_update)
      
      break
    except Exception as err:
      print(err)

create()
