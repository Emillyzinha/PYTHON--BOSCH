def decimal():
    dec = int(input("Digite um número em decimal para a transformação em binário: "))
    count = 0
    lista = []

    while count > 0:
        dec = dec/2
        resto = dec%2
        resto = int(resto)
        lista.append(resto)
        count -=1
    print(lista)
if __name__=='__main__':
    decimal()