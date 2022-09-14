def bin():
    binario = int(input("Digite um número binário para transformação em decimal:")) #1011
    tamanho = len(str(binario)) #3
    decimal = 0 #1
    expoente = 0 #1
    while tamanho >= 0:
        resto = binario%10 #1
        decimal = decimal+resto*2**expoente
        tamanho-=1
        expoente+=1
        binario = binario//10
    print(decimal)

if __name__=="__main__":
    bin()