def menu():
    lista = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print("------------ JOGO DA VELHA ------------")
    while True:
        try:
            jogador_um = int(input("[1] - O\n"
                                   "[2] - X\n"
                                   "Você é o jogador 1, escolha a opção acima desejada: "))
            if jogador_um == 1:
                print("\nA opção de jogo para o jogador 1 é jogador 2 o 'O'"
                      "\nA opção de jogo para o jogador 2 é jogador 2 o 'X'.")
                break
            elif jogador_um == 2:
                print("\nA opção de jogo para o jogador 1 é jogador 1 é o 'X'."
                      "\nA opção de jogo para o jogador 2 é jogador 2 o 'O'.")
                break
            if jogador_um > 2 or jogador_um < 1:
                print("Escolha uma das opções apresentadas.\n")
                continue
        except(ValueError):
            print("Digite um número entre as opções apresentadas.\n")

    printjogo(lista)
    while True:
        for i in range(0,9):
            try:
                jogada_efetivada = False
                while jogada_efetivada == False:
                    print("--- JOGADOR 1 ---")
                    opcao_um = int(input("Digite a posição desejada: "))
                    jogada_efetivada = substituicao(opcao_um, opcao_dois=None, lista=lista)
                    printjogo(lista)
                    jogoVelha(lista)
            except(ValueError):
                print("Digite uma das opções apresentadas.")
                return

            try:
                jogada_efetivada = False
                while jogada_efetivada == False:
                    print("--- JOGADOR 2 ---")
                    opcao_dois = int(input("Digite a posição desejada: "))
                    jogada_efetivada = substituicao(opcao_um=None, opcao_dois=opcao_dois, lista=lista)
                    printjogo(lista)
            except(ValueError):
                print("Digite uma das opções apresentadas.")
                return opcao_dois



def substituicao(opcao_um, opcao_dois, lista):
    jogada_efetiva = False

    for linha in range(0, 3):
        if opcao_um in lista[linha]: #SE O NÚMERO 1 ELE ESTÁ DISPONÍVEL PRA SER JOGADOR
            posicao = lista[linha].index(opcao_um)
            lista[linha][posicao] = "O"
            jogada_efetiva = True

    for linha in range(0, 3):
        if opcao_dois in lista[linha]:
            posicao = lista[linha].index(opcao_dois)
            lista[linha][posicao] = "X"
            jogada_efetiva = True

    if jogada_efetiva == False:
        print("Digite outra opção disponível.")

    return jogada_efetiva

def printjogo(lista):
    print(f"\n {lista[0][0]} | {lista[0][1]} | {lista[0][2]}\n"
          f" {lista[1][0]} | {lista[1][1]} | {lista[1][2]}\n"
          f" {lista[2][0]} | {lista[2][1]} | {lista[2][2]}\n")

def jogoVelha(lista):
    for linha1 in range(0, 3):
        if lista[linha1][0] == "O" and lista[linha1][1] == "O" and lista[linha1][2] == "O":
            print("Você ganhou jogador 1!")
            break
        elif lista[linha1][0] == "X" and lista[linha1][1] == "X" and lista[linha1][2] == "X":
            print("Você ganhou jogador 2!")
            break

    if lista[0][0] == "O" and lista[0][1] == "O" and lista[0][2] == "O":
        print("Você ganhou jogador 1!")
    elif lista[0][0] == "X" and lista[1][1] == "X" and lista[2][2] == "X":
        print("Você ganhou jogador 2!")

    elif lista[2][0] == "O" and lista[1][1] == "O" and lista[0][2] == "O":
        print("Você ganhou jogador 1!")
    elif lista[2][0] == "X" and lista[1][1] == "X" and lista[0][2] == "X":
        print("Você ganhou jogador 2!")

    elif lista[0][0] == "O" and lista[1][0] == "O" and lista[2][0] == "O":
        print("Você ganhou jogador 1!")
    elif lista[0][1] == "O" and lista[1][1] == "O" and lista[2][1] == "O":
        print("Você ganhou jogador 1!")
    elif lista[0][2] == "O" and lista[1][2] == "O" and lista[2][2] == "O":
        print("Você ganhou jogador 1!")

    elif lista[0][0] == "X" and lista[1][0] == "X" and lista[2][0] == "X":
        print("Você ganhou jogador 2!")
    elif lista[0][1] == "X" and lista[1][1] == "X" and lista[2][1] == "X":
        print("Você ganhou jogador 2!")
    elif lista[0][2] == "X" and lista[1][2] == "X" and lista[2][2] == "X":
        print("Você ganhou jogador 2!")

if __name__ == '__main__':
    # jogo_da_velha()
    menu()