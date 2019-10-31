print('\t''='*15)
print('\t\t\t'' 1 - Cadastrar')
print('\t\t\t'' 2 - Listar')
print('\t\t\t'' 3 - Sair')
print('\t''='*15)
resp = input('\n Escolha: ')

Cadastro = list()

while resp != 3:

    if resp == '1':
        nome = input('Digite nome : ')
        idade = input('Digite Idade: ')
        sexo = input('Sexo (F)(M): ')
        email = input('Digite email: ')
        Pessoa = {
            'nome': nome,
            'idade': idade,
            'sexo': sexo,
            'email': email
        }
        Cadastro.append(Pessoa)
        resp = input('Opção: ')
    elif resp == '2':
        print(Cadastro)
        resp = input('Opção: ')
    else:
        break;
