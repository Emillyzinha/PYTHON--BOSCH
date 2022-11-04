import random
import time


class Jogo_dado:
    def __init__(self, nome, credito, jogada_computador, jogada_usuario):
        self.credito = credito
        self.jogada_computador = jogada_computador
        self.jogada_usuario = jogada_usuario
        self.nome = nome


def jogo_inicio():
    print("--------------- JOGO DE DADOS ----------------")
    nome = input("Escreva como gostaria de ser chamado(a): ").title()
    print("Cada jogada tem o valor de R$ 2,00.")
    credito = int(input("Digite a quantidade de crédito desejada: "))
    while credito % 2 != 0:
        print("Não aceitamos créditos que sejam diferentes de números pares.")
        credito = int(input("Digite a quantidade de crédito desejada: "))

    jogada_usuario = int(input(nome + ", digite a sua jogada (1-6): "))

    while jogada_usuario > 6 or jogada_usuario < 1:
        jogada_usuario = int(input(nome + ", digite a sua jogada entre um intervalo de 1 a 6 números: "))
    jogada_computador = random.randint(1, 6)

    while jogada_computador == jogada_usuario:
        jogada_computador = random.randint(1, 6)
    print("Lado jogado pelo computador: ", jogada_computador)

    jogadas(credito, jogada_computador, jogada_usuario, nome)


def jogadas(credito, jogada_computador, jogada_usuario, nome):
    credito -= 2
    print("\n----------- O JOGO COMEÇOU -----------")
    print("Dado jogado, aguarde....")
    time.sleep(5)
    lado_dado = random.randint(1, 6)

    if lado_dado == jogada_usuario:
        credito += 4
        print("Parabéns " + nome + "! Você ganhou.")
        print(" [1] - Sim")
        print(" [2] - Não")
        input("Escolha a opção desejada para uma revanche: ")

    elif lado_dado == jogada_computador:
        print("\n----------- O DOBRO OU NADA -----------")
        print("Ish, o computador venceu e ele deseja uma revanche. Você aceita?")
        print(" [1] - Sim"
              " [2] - Não")
        decisao_revanche = int(input("Digite a opção desejada: "))
        while decisao_revanche > 2 or decisao_revanche < 1:
            print(" [1] - Sim\n"
                  " [2] - Não")
            decisao_revanche = input("Digite uma das opção desejada: ")
            if decisao_revanche == 1:
                revanche(nome, jogada_usuario, jogada_computador)
            elif decisao_revanche == 2:
                break

    else:
        print("Por enquanto ninguém venceu. Aguarde, vamos jogar novamente o dado....")
        time.sleep(5)
        jogadas(credito, jogada_computador, jogada_usuario, nome)


def revanche(nome, jogada_usuario, jogada_computador):
    jogada_usuario = int(input(nome + ", digite a sua jogada (1-6): "))
    while jogada_usuario > 6 or jogada_usuario < 1:
        jogada_usuario = int(input(nome + ", digite a sua jogada entre um intervalo de 1 a 6 números: "))
    jogada_computador = random.randint(1, 6)

    while jogada_computador == jogada_usuario:
        jogada_computador = random.randint(1, 6)
    print("Lado jogado pelo computador: ", jogada_computador)
    jogadas(jogada_computador, jogada_usuario, nome)


if __name__ == '__main__':
    jogo_inicio()
