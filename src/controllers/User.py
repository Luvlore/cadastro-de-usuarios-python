import csv

from prettytable import PrettyTable
from utils.clear_screen import clear_screen
from utils.formatter import formatter
from utils.validations import (validate_birthdate, validate_cpf,
                               validate_email, validate_phone)

genders = ['feminino', 'masculino', 'outro']

field_names_table = ['ID', 'Nome', 'Gênero', 'Email', 'Telefone', 'CPF', 'Data de Nascimento']

def find_all():
  clear_screen()
  with open('src/database/users.csv', 'r') as file:
    users = csv.DictReader(file)
    
    table = PrettyTable()
    table.title = 'TODOS USUÁRIOS LISTADOS'
    table.field_names = field_names_table
    
    for pos, user in enumerate(users):
      table.add_row([pos, *user.values()])
    
    print(table)
    
    pass
  
  input('')

def find_by_name():
  clear_screen()
  
  with open('src/database/users.csv', 'r') as file:
    name = input('Digite o nome: ')
    
    users = csv.DictReader(file)
    
    table = PrettyTable()
    table.title = 'USUÁRIOS ENCONTRADOS'
    table.field_names = field_names_table
    
    for pos, user in enumerate(users):
      if name.lower() in user['name'].lower():
        table.add_row([pos, *user.values()])
        
    print(table)
    pass

  input('')

def create():
  new_user = {'name': '', 'gender': '', 'email': '', 'phone': '', 'cpf': '', 'birthdate': ''}
  
  is_create = False
  
  while not is_create:
    clear_screen()
    
    print('CRIAÇÃO DE NOVO USUÁRIO')
    
    while True:
      try:
        new_user['name'] = input('Digite seu primeiro nome: ').strip().capitalize()
        
        if not new_user['name'].isalpha():
          raise Exception('Formato de nome incorreto')
        
        break
      except Exception as err:
        print(err)
    
    while True:
      try:
        for pos, gender in enumerate(genders): 
          print(f'{pos + 1:02}: {gender}')
        
        escolha = input('Escolha seu gênero: ') 
        
        if not escolha.isdigit() or int(escolha) not in list(range(1, len(genders) + 1)):
          raise ValueError('Digite um valor válido')
        
        new_user['gender'] = genders[int(escolha) - 1]
        break
      except ValueError as err:
        print(err)
        
    while True:
      try:
        new_user['email'] = input('Digite seu email: ')
        
        if not validate_email(new_user['email']):
          raise Exception('Digite um email válido')
        
        break
      except Exception as err:
        print(err)
    
    while True:
      try:
        phone = input('Digite seu número de telefone: ')
        new_user['phone'] = validate_phone(phone)
        break
      except Exception:
        print('Formato de telefone inválido!')
      
    while True:
      try:
        cpf = input('Digite seu CPF: ')
        new_user['cpf'] = validate_cpf(cpf)
        break
      except Exception as err:
        print(err)
    
    while True:
      try:
        birthdate = input('Digite sua data de nascimento: ')
        new_user['birthdate'] = validate_birthdate(birthdate)
        break
      except Exception:
        print('Formato de data incorreto ou inválido. Por favor, digite no formato: DD/MM/AAAA')
    
    clear_screen()
    
    table = PrettyTable()
    table.title = 'USUÁRIO CRIADO'
    table.field_names = field_names_table[1:]
    table.add_row(new_user.values())
    
    print(table)
  
    resp = ' '
    
    while resp not in 'SN':
      resp = input('As informações conferem? ').strip().upper()[0]
      
      if resp == 'S':
        with open('src/database/users.csv', 'a') as file:
          
          fieldnames = new_user.keys()
          writer = csv.DictWriter(file, fieldnames)
          
          writer.writerow(new_user)
          
          pass
        
        is_create = True

def delete():
  find_user = {
    'Ver lista de todos os usuário': find_all,
    'Encontrar usuário pelo nome': find_by_name
  }
  
  for pos, op in enumerate(find_user.keys()):    
    print(f'{pos + 1}: {op}')

  choice = input('O que deseja fazer? ')
  
  if not int(choice) or int(choice) not in list(range(1, len(find_user) + 2)):
    raise ValueError('Digite uma opção válida!')
  
  if int(choice) in list(range(1, len(find_user) + 1)):
    for pos, op in enumerate(find_user.values()):
      if pos + 1 == int(choice):
        op()
  
  print('Digite 0 para cancelar.')
  user_to_delete = input('Escolha o usuário que deseja deletar pelo ID: ')
  
  with open('src/database/users.csv', 'r') as file:
    users = csv.DictReader(file)
    new_users = []
    
    for pos, user in enumerate(users):
      if int(user_to_delete) != pos:
        new_users.append(user)
    
    for user in new_users:
      fieldnames = user.keys()
      csv.DictWriter(new_users, fieldnames)
    print(new_users)
