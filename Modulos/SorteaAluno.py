import random
aluno1 = input('Digite o nome do aluno: ')
aluno2 = input('Digite o nome do aluno: ')
aluno3 = input('Digite o nome do aluno: ')
aluno4 = input('Digite o nome do aluno: ')
alunos = [aluno1, aluno2, aluno3, aluno4]
escolhido = random.choice(alunos)
print('O aluno escolhido foi {}'.format(escolhido))
