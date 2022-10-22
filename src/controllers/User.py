import csv

from utils.formatter import formatter
from utils.validations import validate_email, validate_phone

genders = ['feminino', 'masculino', 'outro']

def find_all():
  with open('src/database/users.csv', 'r') as file:
    users = csv.DictReader(file)
    
    for user in users:
      print(formatter(user))
    
    pass

def find_by_name(name):
  with open('src/database/users.csv', 'r') as file:
    users = csv.DictReader(file)
    
    print('USUÁRIOS ENCONTRADOS\n')
    for user in users:
      if name.lower() in user['name'].lower():
        print(formatter(user))

def create():
  new_user = {}
  
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
    # new_user['cpf']       = input('Digite seu CPF: ')
    # new_user['birthdate'] = input('Digite sua data de nascimento: ')
