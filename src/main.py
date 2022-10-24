'''
menu do sistema
'''
from utils import print_users

n1 = '[1]Imprima a lista de usuários\n'
n2 = '[2]Busque um usuário pelo nome\n'
n3 = '[3]Cadastre um novo usuário\n'
n4 = '[4]Remova um usuário\n'
n5 = '[5]Atualize um usuário\n'
bonus = '[6]Estátisticas do sistema\n'
quit = '[7]Encerrar o sistema\n'
menu = f'Digite o número da ação a ser realizada:\n{n1}{n2}{n3}{n4}{n5}{bonus}{sair}'

action = input(menu)

while action != '7':
    if action == '1':
        print(print_users(data))
