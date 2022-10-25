import csv

from prettytable import PrettyTable
from utils.clear_screen import clear_screen
from utils.finders import find_id, menu_find
from utils.validations import *

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

def create(id=False, users=False):
  user_update = users[id].split(',') if id else []
  
  new_user = {
    'name': user_update[0] if id else '',
    'gender': user_update[1] if id else '',
    'email': user_update[2] if id else '',
    'phone': user_update[3] if id else '',
    'cpf': user_update[4] if id else '',
    'birthdate': user_update[5] if id else ''
  }
  
  fields_functions = {
    'name': {'name': 'o nome', 'func': validate_name},
    'gender': {'name': 'o gênero', 'func': validate_gender},
    'email': {'name': 'o email', 'func': validate_email},
    'cpf': {'name': 'o CPF', 'func': validate_cpf},
    'phone': {'name': 'o telefone', 'func': validate_phone},
    'birthdate': {'name': 'a data de nascimento', 'func': validate_birthdate},
  }
  
  while True:
    clear_screen()
    
    print(f'{"ATUALIZAÇÃO" if id else "CRIAÇÃO"} DE NOVO USUÁRIO')
    
    for pos, (opKey, op) in enumerate(fields_functions.items()):
      if id:
        change = ' '
        
        while change not in 'SN':
          change = input(f'Deseja mudar {op["name"]}? [S/N] ').strip().upper()[0]
        
        if change == 'S':
          new_user[opKey] = op['func']()
      else:
        new_user[opKey] = op['func']()
    
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
              updated = f"{','.join(list(new_user.values()))}"
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
     
      create(id, users[1:])
      
      break
    except Exception as err:
      print(err)

def statistics():
  with open('src/database/users.csv', 'r') as file:
    all_users = list(csv.DictReader(file))
    all_females = [user for user in all_users if user['gender'] == gender]
    all_males = [user for user in all_users if user['gender'] == 'masculino']
    all_minors = [user for user in all_users if user['birthdate']]
    all_majors = []
    all_seniors = []
    
    
    input()
  return None

statistics()
