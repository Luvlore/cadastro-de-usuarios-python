def formatter(user):
  return f'Nome: {user["name"]}\n' \
         f'Gênero: {user["gender"]}\n' \
         f'Email: {user["email"]}\n' \
         f'Telefone: {user["phone"]}\n'\
         f'CPF: {user["cpf"]}\n'\
         f'Data de Nascimento: {user["birthdate"]}\n'
