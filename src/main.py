from prettytable import PrettyTable

from controllers.User import *
from utils.validations import validate_phone

menu = {
  'Mostrar todos os usuários': find_all,
  'Encontrar um usuário pelo nome': find_by_name,
  'Criar novo usuário': create,
  'Deleter um usuário': delete,
  'Atualizar um usuário': update,
}

while True:
  try:
    table = PrettyTable()
    
    table.title = 'SISTEMA DE GERENCIAMENTO DE USUÁRIOS'
    table.field_names = ['ID', 'Operação']
    
    for pos, op in enumerate(menu.keys()):
      table.add_row([pos + 1, op])
    table.add_row([len(menu) + 1, 'Sair'])

    clear_screen()
    print(table)
    
    choice = input('O que deseja fazer? ')
    
    if not choice.isdigit() or int(choice) not in list(range(1, len(menu) + 2)):
      raise ValueError('Digite uma opção válida!')
    
    if int(choice) in list(range(1, len(menu) + 1)):
      for pos, op in enumerate(menu.values()):
        if pos + 1 == int(choice):
          op()
    
    else:
      print('FIM DO PROGRAMA')
      break
  except Exception as err:
    print(err)
    input()
