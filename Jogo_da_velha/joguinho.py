def jogoVelha():
    print("----------- BEM VINDO AO JOGO DA VELHA -----------")
    jogo1 = [1, 2, 3]
    jogo2 = [4, 5, 6]
    jogo3 = [7, 8, 9]

    print("Jogador 1 é 'O'.")
    print("Jogador 2 é 'X'.")
    printJogo(jogo1, jogo2, jogo3)

    print("----- JOGADOR 1 -----")
    jogadorUm = int(input("Digite em qual posição você quer jogar: "))
    printJogo(jogo1, jogo2, jogo3)
    substituindo1(jogadorUm, jogo1, jogo2, jogo3)

    print("----- JOGADOR 2 -----")
    jogadorDois = int(input("Digite em qual posição você quer jogar: "))
    printJogo(jogo1, jogo2, jogo3)
    substituindo2(jogadorDois, jogo1, jogo2, jogo3)


def substituindo1(jogador1, lista1, lista2, lista3):
    while lista1[jogador1] == "O" or lista2[jogador1] == "O" or lista3[jogador1] == "O":
        print("Digite uma posição que não esteja ocupada1.")
        return jogador1
    else:
        if jogador1 in lista1:
            lista1[jogador1] = "O"
            print(lista1)
            # pos1 = lista1.index(jogador1)
            # lista1[jogador1].insert(pos1, "O")
        elif jogador1 in lista2:
            pos2 = lista2.index(jogador1)
            lista2[jogador1].insert(pos2, "O")
        elif jogador1 in lista3:
            pos3 = lista3.index(jogador1)
            lista3[jogador1].insert(pos3, "O")

def substituindo2(jogador2, lista1, lista2, lista3):
    while lista1[jogador2] == "X" or lista1[jogador2] == "X" or lista1[jogador2] == "X":
        print("Digite uma posição que não esteja ocupada2.")
        return jogador2
    else:
        if jogador2 in lista1:
            pos1 = lista1.index(jogador2)
            lista1[jogador2].insert(pos1, "X")
        elif jogador2 in lista2:
            pos2 = lista2.index(jogador2)
            lista2[jogador2].insert(pos2, "X")
        elif jogador2 in lista3:
            pos3 = lista3.index(jogador2)
            lista3[jogador2].insert(pos3, "X")


def printJogo(lista1, lista2, lista3):
    for i in range(len(lista1)):
        print(f" {lista1[i]} |", end="")
    print("")

    for i in range(len(lista2)):
        print(f" {lista2[i]} |", end="")
    print("")

    for i in range(len(lista3)):
        print(f" {lista3[i]} |", end="")
    print("")
    print("\n")


if __name__ == '__main__':
    jogoVelha()