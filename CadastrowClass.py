class Pessoa:

    def __init__(self, nome, email, idade):
        self.nome = nome
        self.email = email
        self.idade = idade

    
class CRUD:

    Pessoa = []

    def cadastrar_Pessoa(self):

        nome = input('Digite seu nome: ')
        email = input('Digite seu Email: ')
        idade = input('Qual sua Idade: ')

        self.Pessoa.append(Pessoa(nome, email, idade))
        print('\n\nCadastro Realizado!\n')

    def listar_Pessoas(self):
        for i, Pessoa in enumerate(self.Pessoa):
            print('\n')
            print(Pessoa.nome, Pessoa.email, Pessoa.idade)

    def loop(self):
        while True:
            print('='*30)
            print(' 1 - Listar Pessoas')
            print(' 2 - Cadastrar Pessoa')
            print('='*30)
            resp = input('Escolha: ') 
            if resp == '1':
                self.listar_Pessoas()
            elif resp == '2':
                self.cadastrar_Pessoa()
            else:
                print('Tente Outra Vez!')
                continue


if __name__ == '__main__':
    interface = CRUD()
    interface.loop()