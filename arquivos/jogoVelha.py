import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PyQt5 import QtGui


class Velha(QMainWindow):
    def __init__(self):
        super().__init__()
        self.topo = 100
        self.esquerda = 100
        self.largura = 1000
        self.altura = 600
        self.lista_jogadas = []

        self.verificacao1 = False
        self.verificacao2 = False
        self.verificacao3 = False
        self.verificacao4 = False
        self.verificacao5 = False
        self.verificacao6 = False
        self.verificacao7 = False
        self.verificacao8 = False
        self.verificacao9 = False

        self.fundo = QLabel(self)
        self.fundo.move(0, 0)
        self.fundo.resize(1000, 600)
        self.fundo.setScaledContents(True)
        self.fundo.setPixmap(QtGui.QPixmap('img/interface/velha.jpg'))

        self.botao1 = QPushButton(self)
        self.botao1.move(325, 120)
        self.botao1.resize(100, 100)
        self.botao1.clicked.connect(self.verifica1)

        # self.botao1.setFlat(True) # para o botão ficar visível
        # self.botao1.clicked.connect(lambda: self.jogadas(1))

        self.botao2 = QPushButton(self)
        self.botao2.move(450, 120)
        self.botao2.resize(100, 100)
        self.botao2.clicked.connect(self.verifica2)


        self.botao3 = QPushButton(self)
        self.botao3.move(572, 120)
        self.botao3.resize(100, 100)
        self.botao3.clicked.connect(self.verifica3)

        self.botao4 = QPushButton(self)
        self.botao4.move(325, 250)
        self.botao4.resize(100, 100)
        self.botao4.clicked.connect(self.verifica4)

        self.botao5 = QPushButton(self)
        self.botao5.move(450, 250)
        self.botao5.resize(100, 100)
        self.botao5.clicked.connect(self.verifica5)

        self.botao6 = QPushButton(self)
        self.botao6.move(572, 250)
        self.botao6.resize(100, 100)
        self.botao6.clicked.connect(self.verifica6)

        self.botao7 = QPushButton(self)
        self.botao7.move(325, 380)
        self.botao7.resize(100, 100)
        self.botao7.clicked.connect(self.verifica7)

        self.botao8 = QPushButton(self)
        self.botao8.move(450, 380)
        self.botao8.resize(100, 100)
        self.botao8.clicked.connect(self.verifica8)

        self.botao9 = QPushButton(self)
        self.botao9.move(572, 380)
        self.botao9.resize(100, 100)
        self.botao9.clicked.connect(self.verifica9)

        self.carregar_janela()

    def jogo(self):
        if len(self.lista_jogadas) == 0:
            self.lista_jogadas.append(1)
        if self.lista_jogadas[0] == 1:
            self.lista_jogadas.append(2)
        elif self.lista_jogadas[0] == 2:
            self.lista_jogadas.append(1)
        self.lista_jogadas.reverse()

        if self.verificacao1:
            self.botao1.setEnabled(False)
            self.verificacoes(self.botao1)
            self.verificacao1 = False
            # self.botao1.setPixmap(QtGui.QPixmap('X.png'))
        elif self.verificacao2:
            self.botao2.setEnabled(False)
            self.verificacoes(self.botao2)
            self.verificacao2 = False
        elif self.verificacao3:
            self.botao3.setEnabled(False)
            self.verificacoes(self.botao3)
            self.verificacao3 = False

        elif self.verificacao4:
            self.botao4.setEnabled(False)
            self.verificacoes(self.botao4)
            self.verificacao4 = False
        elif self.verificacao5:
            self.botao5.setEnabled(False)
            self.verificacoes(self.botao5)
            self.verificacao5 = False
        elif self.verificacao6:
            self.botao6.setEnabled(False)
            self.verificacoes(self.botao6)
            self.verificacao6 = False

        elif self.verificacao7:
            self.botao7.setEnabled(False)
            self.verificacoes(self.botao7)
            self.verificacao7 = False
        elif self.verificacao8:
            self.botao8.setEnabled(False)
            self.verificacoes(self.botao8)
            self.verificacao8 = False
        elif self.verificacao9:
            self.botao9.setEnabled(False)
            self.verificacoes(self.botao9)
            self.verificacao9 = False

        else:
            print('não deu certo')


    #     PRECISO passar a verificacao como a verificacao do BOTÃO

    def verificacoes(self, botao):
        if self.lista_jogadas[0] == 1:
            botao.setStyleSheet('border-image: url(O.png)')
        elif self.lista_jogadas[0] == 2:
            botao.setStyleSheet('border-image: url(X.png)')

        print(str(f'deu certo e o botão é o {botao}'))

        print(self.lista_jogadas)

    def verifica1(self):
        self.verificacao1 = True
        self.jogo()

    def verifica2(self):
        self.verificacao2 = True
        self.jogo()

    def verifica3(self):
        self.verificacao3 = True
        self.jogo()

    def verifica4(self):
        self.verificacao4 = True
        self.jogo()

    def verifica5(self):
        self.verificacao5 = True
        self.jogo()

    def verifica6(self):
        self.verificacao6 = True
        self.jogo()

    def verifica7(self):
        self.verificacao7 = True
        self.jogo()

    def verifica8(self):
        self.verificacao8 = True
        self.jogo()

    def verifica9(self):
        self.verificacao9 = True
        self.jogo()
    # definir o parametro como o valor da variavel

    def carregar_janela(self):
        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
        self.show()


if __name__ == '__main__':
    aplicacao = QApplication(sys.argv)
    v = Velha()
    sys.exit(aplicacao.exec())
