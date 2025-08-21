#Para acessa um sistema, o usario deve digitar o username darth_vader e a senha 1138
#crie um script que recebe e valide esta informação de acesso

username = input("Digite o seu nome de Usuário: ")
senha = input("Digite a sua senha: ")

if username.lower() == "darth_vader" and senha == "1138":
    print("Login bem sucedido!")
else:
    print("Login não autorizado")