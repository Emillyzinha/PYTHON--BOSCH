# é um numero primo? com laço de repetição
# se não for primo: mostrar todos os divisores do número
import time

def ex1 ():
    while True:
        n = int(input("Digite um número: "))
        if n % n == 0 and n % 2 != 0:
            print("É um número primo")
        try:
            break
        # else:
        #     print("Não é um número primo")


if __name__ == '__main__':
    time.sleep(5)
    ex1()