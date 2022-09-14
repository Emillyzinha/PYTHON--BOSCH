from datetime import datetime

dia1 = datetime.now().day
mes1 = datetime.now().month

dia = int(input("Me diga o dia do seu nascimento: "))
# dia = int(dia)
mes = int(input("Me diga o mês do seu nascimento: "))
# mes = int(mes)
ano = int(input("Me diga o ano do seu nascimento: "))
# ano = int(ano)

if (ano <= 2004 and mes <= mes1 and dia <= dia1):
    print("Pode tirar a CNH!")
else:
    print("Você não pode tirar a CNH")
