def menu_find(find_user):
  for pos, op in enumerate(find_user.keys()):    
    print(f'{pos + 1}: {op}')

  choice = input('O que deseja fazer? ')
  
  if int(choice) in list(range(1, len(find_user) + 1)):
    for pos, op in enumerate(find_user.values()):
      if pos + 1 == int(choice):
        op()

def find_id(users):
  id = input('Escolha o usuário que pelo ID: ')
        
  if not id.isdigit() or int(id) not in list(range(0, len(users) - 1)):
    raise ValueError('Digite um ID válido!')

  return int(id)
