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

#3
class Televisao:
    def __init__(self):
        self.volume = 0
        self.canal = 1
    def consultar_volume(self):
        print(f'o volume atual é: {self.volume}')
    
    def consultar_canal(self):
        print(f'o canal atual é {self.canal}')

    def trocar_canal(self, novo_canal):
        novo_canal = int(input("coloque o canal específico: "))
        self.canal = novo_canal

class controle(Televisao):
    def __init__(self):
        super().__init__()        
    
    def aumentar_volume(self):
        if self.volume < 100:
            self.volume += 1


    def diminuir_volume(self):
        if self.volume >= 0:
            self.volume -= 1

    def trocar_canal(self, novo_canal):
        novo_canal = int(input("coloque o canal específico: "))
        self.canal = novo_canal
    def aumentar_canal(self):
        if self.canal < 160:
            self.canal += 1
    def diminuir_canal(self):
        if self.canal > 1:
            self.canal -= 1
    


