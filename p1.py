#1
class Pessoa:
    def __init__(self, nome):
        self.nome = nome

class Professor(Pessoa):
    def __init__(self, nome, titulacao):
        super().__init__(nome)
        self.titulacao = titulacao

#2
class Tamagushi:
    def __init__(self, nome):
        self.nome = nome
        self.fome = 100
        self.saude = 100
        self.idade = 0
    def alterar_nome(self):
        novo_nome = input("Coloque o novo nome")
        self.nome = novo_nome
    def alterar_fome(self):
        nova_fome = int(input("Coloque a nova fome"))
        self.fome = nova_fome
    def alterar_saude(self):
        nova_saude = int(input("Coloque a nova saúde"))
        self.saude = nova_saude
    def alterar_idade(self):
        nova_idade = int(input("Coloque a nova idade"))
        self.idade = nova_idade
    def set_humor(self):
        humor = self.fome + self.saude
        print(f'o humor do nosso tamaguchi é {humor}')

    def retorna_nome(self):
        print(f'o nome do nosso tamaguchi é :{self.nome}')

    def retorna_fome(self):
        print(f'a fome do nosso tamaguchi é :{self.fome}')

    def retorna_saude(self):
        print(f'a saude do nosso tamaguchi é :{self.saude}')
    
    def retorna_idade(self):
        print(f'a idade do nosso tamaguchi é :{self.idade}')

a = Tamagushi('Cris')
a.alterar_fome()
a.alterar_nome()
a.alterar_saude()
a.alterar_idade()
a.set_humor()
a.retorna_fome()
a.retorna_idade()
a.retorna_nome()
a.retorna_saude()
