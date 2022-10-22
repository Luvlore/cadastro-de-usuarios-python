import csv

from utils.formatter import formatter


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
