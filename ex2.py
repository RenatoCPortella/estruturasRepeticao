# nome = ''
# senha = ''
#
# while senha == nome:
#     nome = input('Digite um nome: ')
#     senha = input('Digite uma senha: ')
#     print('A senha nao deve ser igual ao nome!')
#
# print('Usuario e senha validos!')

while True:
    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a sua senha: ")

    if usuario == senha:
        print("Erro, tente novamente")
    else:
        print("Sucesso!")
        break
