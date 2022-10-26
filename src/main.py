from prettytable import PrettyTable

from controllers.User import (create, delete, find_all, find_by_name,
                              statistics, update)
from utils.clear_screen import clear_screen
from utils.validations import validate_phone

menu = {
  'Criar novo usuário': create,
  'Mostrar todos os usuários': find_all,
  'Encontrar um usuário pelo nome': find_by_name,
  'Atualizar um usuário': update,
  'Deleter um usuário': delete,
  'Estatísticas dos usuários': statistics
}

while True:
  try:
    table = PrettyTable()
    
    table.title = 'SISTEMA DE GERENCIAMENTO DE USUÁRIOS'
    table.field_names = ['   ', 'Operação']
    
    for pos, op in enumerate(menu.keys()):
      table.add_row([f'{pos + 1:02}', op])

    table.add_row([f'{len(menu) + 1:02}', 'Sair'])

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
