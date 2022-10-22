import csv


def find_all():
  with open('src/database/users.csv', 'r') as file:
    users = file.readlines()[1:]
    
    for user in users:
      print(user)
    
    pass

