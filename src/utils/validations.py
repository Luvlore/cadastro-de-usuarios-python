import re
from datetime import date, datetime

from validate_docbr import CPF


def validate_name():
  while True:
    try:
      name = input('Digite seu primeiro nome: ').strip().capitalize()
      
      if not name.isalpha():
          raise Exception('Formato de nome incorreto')
        
      return name
    except Exception as err:
      print(err)

def validate_gender(genders):
  for pos, gender in enumerate(genders): 
          print(f'{pos + 1:02}: {gender}')

  while True:
    try:
      choice = input('Escolha seu gênero: ').strip()
      
      if not choice.isdigit() or int(choice) not in list(range(1, len(genders) + 1)):
          raise ValueError('Digite um valor válido')
        
      return genders[int(choice) - 1]
    except Exception as err:
      print(err)

def validate_email():
  while True:
    try:
      email = input('Digite seu email: ').strip()
      email_format = '^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$'
      
      if not re.match(email_format, email):
        raise Exception('Digite um email válido')       
       
      return email
    except Exception as err:
      print(err)

def validate_phone():
  types = ['Fixo', 'Móvel']
  
  for pos, type in enumerate(types):
    print(f'{pos + 1:02}: {type}')

  while True:
    try:
      choice = input('Escolha o tipo de número: ')
      
      if not choice.isdigit() or int(choice) not in list(range(1, 3)):
        raise Exception('Opção inválida')
      
      type_chosen = types[int(choice)]
      break
    except Exception as err:
      print(err)
  
  while True:
    try:
      phone = input('Digite seu número de telefone: ').strip()
      pattern = '([0-9]{2})(9)?([0-9]{4})([0-9]{4})'
      res = re.search(pattern, phone)
      
      return f'({res.group(1)}) {res.group(2) if res.group(2) else "9"} {res.group(3)}-{res.group(4)}'
    except Exception:
      print('Formato de telefone incorreto!')

def validate_cpf():  
  while True:
    try:
      cpf = input('Digite seu CPF: ')
      cpf_regex = '[0-9]{3}\.?[0-9]{3}\.?[0-9]{3}\-?[0-9]{2}'
      
      if len(cpf) != 11 or not re.match(cpf_regex, cpf):
        raise Exception('Formato de CPF inválido')
      
      if not CPF().validate(cpf):
        raise Exception('CPF inválido')
      
      return cpf
    except Exception as err:
      print(err)

def validate_birthdate():
  while True:
    try:
      birthdate = input('Digite sua data de nascimento: ')
      birthdate_validate = datetime.strptime(birthdate, '%d/%m/%Y')
      today = datetime.now()
      
      if birthdate_validate > today:
        raise Exception()
      
      return birthdate
    except Exception:
      print('Formato de data incorreto ou inválido. Por favor, digite no formato: DD/MM/AAAA')
  
