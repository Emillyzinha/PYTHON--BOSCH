def divisao ():
    a = int(input("Entre com o valor do divisor: "))
    b = int(input("Entre com o valor do dividendo: "))
    result = a/b
    print("O resultado é: ", result)
    print("O tipo de resultado é: ", type(result))

if __name__ == '__main__':
    divisao()