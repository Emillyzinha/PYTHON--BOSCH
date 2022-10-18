# def jogo_da_velha():

def menu():
    lista = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print("------------ JOGO DA VELHA ------------")
    while True:
        try:
            jogador_um = int(input("[1] - O\n"
                                   "[2] - X\n"
                                   "Você é o jogador 1, escolha a opção acima desejada: "))
            if jogador_um == 1:
                print("Você é o jogador 2, sua opção para jogo é o 'X'.")
                break
            elif jogador_um == 2:
                print("Você é o jogador 2, sua opção para jogo é o 'O'.")
                break
            if jogador_um > 2 or jogador_um < 1:
                print("Escolha uma das opções apresentadas.\n")
                continue
        except(ValueError):
            print("Digite um número entre as opções apresentadas.\n")
    printjogo(lista)

    for i in range(0,9):
        print("--- JOGADOR 1 ---")
        opcao_um = int(input("Digite a posição desejada: "))
        substituicao(opcao_um, opcao_dois="", lista=lista)
        printjogo(lista)
        vencer(lista)

        print("--- JOGADOR 2 ---")
        opcao_dois = int(input("Digite a posição desejada: "))
        substituicao(opcao_um, opcao_dois, lista)
        printjogo(lista)


def substituicao(opcao_um, opcao_dois, lista):
    for linha in range(0, 3):
        if opcao_um in lista[linha]:
            posicao = lista[linha].index(opcao_um)
            while opcao_um in lista[linha] == "X" or opcao_um in lista[linha] == "O":
                print("Digite outra opção disponível.")
            else:
                lista[linha][posicao] = "O"

    # [linha][posicao]
    # [linha][posicao]

    for linha in range(0, 3):
        if opcao_dois in lista[linha]:
            posicao = lista[linha].index(opcao_dois)
            if lista[linha][posicao] == "X" or lista[linha][posicao] == "O":
                print("Digite outra opção disponível.")
            else:
                lista[linha][posicao] = "X"

def vencer(lista):
    for linha1 in range(0,3):
        if lista[linha1][0] and lista[linha1][1] and lista[linha1][2] == "O":
            print("Você ganhou jogador 1!")
        elif lista[linha1][0] and lista[linha1][1] and lista[linha1][2] == "X":
            print("Você ganhou jogador 2!")
            break

    if lista[0][0] and lista[1][1] and lista[1][2] == "O":
        print("Você ganhou jogador 1!")
    if lista[0][0] and lista[1][1] and lista[1][2] == "X":
        print("Você ganhou jogador 2!")

    if lista[2][0] and lista[1][1] and lista[0][2] == "O":
        print("Você ganhou jogador 1!")
    if lista[2][0] and lista[1][1] and lista[0][2] == "X":
        print("Você ganhou jogador 2!")

    if lista[0][0] and lista[1][0] and lista[2][0] == "O":
        print("Você ganhou jogador 1!")
    if lista[0][1] and lista[1][1] and lista[2][1] == "O":
        print("Você ganhou jogador 1!")
    if lista[0][2] and lista[1][2] and lista[2][2] == "O":
        print("Você ganhou jogador 1!")

    if lista[0][0] and lista[1][0] and lista[2][0] == "X":
        print("Você ganhou jogador 2!")
    if lista[0][1] and lista[1][1] and lista[2][1] == "X":
        print("Você ganhou jogador 2!")
    if lista[0][2] and lista[1][2] and lista[2][2] == "X":
        print("Você ganhou jogador 2!")



def printjogo(lista):
    print(f" {lista[0][0]} | {lista[0][1]} | {lista[0][2]}\n"
          f" {lista[1][0]} | {lista[1][1]} | {lista[1][2]}\n"
          f" {lista[2][0]} | {lista[2][1]} | {lista[2][2]}\n")

if __name__ == '__main__':
    # jogo_da_velha()
    menu()