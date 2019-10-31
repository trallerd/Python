import csv
print('='*30)
print(' 1 - Listar')
print(' 2 - Cadastrar')
print(' 3 - Sair')
print('='*30)
resp = input('Escolha: ')

while resp != 3:
	if resp == '1':
		with open('Cadastro.csv', 'r') as cadastro:
			cadastroFile = csv.reader(cadastro)
			try:
				for linha in cadastro:
					print(linha)
			finally:
				cadastro.close()
		resp = input('Escolha: ')
	elif resp == '2':
		with open('Cadastro.csv', 'a') as novoCadastro:
			f = csv.writer(novoCadastro)
			nome = input('Digite nome: ')
			email = input('Digite email: ')
			f.writerow([nome, email])
		resp = input('Escolha: ')
	else:
		break
