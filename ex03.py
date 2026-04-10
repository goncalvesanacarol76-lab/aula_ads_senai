class Pessoa:
    def __init__(self, nome, idade): #construtora
        self.nome = nome
        self.idade = idade
    def apresentar(self):
        print("Olá", self.nome)
        print("Você tem:", self.idade, "anos")

nome = input("Qual seu nome? ")
idade = input("Qual sua idade? ")
pessoa1 = Pessoa(nome, idade) 
pessoa1.apresentar()