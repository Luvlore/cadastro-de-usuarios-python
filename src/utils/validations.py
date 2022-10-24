import re
from datetime import date, datetime

from validate_docbr import CPF


def validate_email(email):
  email_format = '^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$'
  
  return True if re.match(email_format, email) else False

def validate_phone(phone):
  pattern = '([0-9]{2})(9)?([0-9]{4,5})([0-9]{4})'
  res = re.search(pattern, phone)
  return f'({res.group(1)}) {res.group(2) if res.group(2) else "9"} {res.group(3)}-{res.group(4)}'

def validate_cpf(cpf):  
  cpf_regex = '[0-9]{3}\.?[0-9]{3}\.?[0-9]{3}\-?[0-9]{2}'
  
  if len(cpf) != 11 or not re.match(cpf_regex, cpf):
    raise Exception('Formato de CPF inválido')
  if not CPF().validate(cpf):
    raise Exception('CPF inválido')
  return cpf

def validate_birthdate(birthdate):
  try:
    datetime.strptime(birthdate, '%d/%m/%Y')
    print(datetime.year())
    
    return birthdate
  except Exception:
    print('Formato de data incorreto. Por favor, digite no formato de: DD/MM/AAAA')
  
print(validate_birthdate('22/12/2023'))
