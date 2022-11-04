from datetime import datetime

class Pessoa:
    ano_atual = 2022 #CRIANDO UMA VARIÁVEL PARA A CLASSE TODA. TODAS AS PESSOA VÃO ESTAR NO MESMO ANO. CONTINUO TENDO QUE USAR O SELF DENTRO DA CLASSE
    # A DIFERENÇA É QUE O ano_atual SERVE
    # PARA A CLASSE TODA, ELE NÃO MUDA PARA NENHUMA INSTÂNCIA (2022 PERMANECE SENDO O MESMO ANO ATUAL PARA p1 e p2)

    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome} não pode falar comendo.')
            return #se não colocar o RETURN ele executa o código debaixo

        if self.falando:
            print(f'{self.nome} já está falando')
            return

        print(f'{self.nome} está falando sobre {assunto}.')
        self.falando = True

    def para_falar(self):
        if not self.falando:
            print(f'{self.nome} não está falando.')
            return

        print(f'{self.nome} parou de falar')
        self.falando = False

    def comer(self, alimento):
        if self.comendo: # se for verdadeiro, retorna isso
            print(f'{self.nome} já está comendo.')
            return

        if self.falando:
            print(f'{self.nome} não pode comer falando')
            return

        print(f"{self.nome} está comendo {alimento}.")
        self.comendo = True

    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo')
            return
        print(f'{self.nome} parou de comer')
        self.comendo = False

    def get_ano_nascimento(self):
        return self.ano_atual - self.idade
        pass

        # o SELF representa a instância da Classe na outra página, faz a ligação entre a instância lá para os atributos da Classe
        # https: // www.youtube.com / watch?v = RLVbB91A5 - 8 & list = PLbIBj8vQhvm34qAAEEH_PdL2tMG9rz - P7 & index = 1   MINUTO 17:29 (OTÁVIO MIRANDA CLASSE PYTHON AULA 35)
#         paradigma procedual python
#         paradigma orientado ao objeto python
#         propety python
#         get set python

