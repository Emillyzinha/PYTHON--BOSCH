import random
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PyQt5 import QtGui

class JokenPo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.escolha_computador = ''
        self.topo = 100
        self.esquerda = 100
        self.largura = 1000
        self.altura = 600
        self.papel_jogador = 0
        self.pedra_jogador = 0
        self.tesoura_jogador = 0
        self.papel_computador = 0
        self.pedra_computador = 0
        self.tesoura_computador = 0
        self.lista_computador = []

        self.fundo = QLabel(self)
        self.fundo.move(0, 0)
        self.fundo.resize(1000, 600)
        self.fundo.setScaledContents(True)
        self.fundo.setPixmap(QtGui.QPixmap('img/interface/jokenpo.jpg'))

        self.usuario = QLabel(self)
        self.usuario.move(400, 230)
        self.usuario.resize(280, 200)

        self.computador = QLabel(self)
        self.computador.move(790, 230)
        self.computador.resize(280, 200)

        self.botaoPedra = QPushButton('PEDRA', self)
        self.botaoPedra.move(20, 40)
        self.botaoPedra.resize(200, 170)
        self.botaoPedra.clicked.connect(self.mostra_pedra)

        self.botaoTesoura = QPushButton('TESOURA', self)
        self.botaoTesoura.move(20, 220)
        self.botaoTesoura.resize(200, 170)
        self.botaoTesoura.clicked.connect(self.mostra_tesoura)

        self.botaoPapel = QPushButton('PAPEL', self)
        self.botaoPapel.move(20, 390)
        self.botaoPapel.resize(210, 200)
        self.botaoPapel.clicked.connect(self.mostra_papel)

        self.carregar_janela()

    def carregar_janela(self):
        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
        self.show()

    def mostra_papel(self):
        self.usuario.setPixmap(QtGui.QPixmap('img/interface/papel.png'))
        self.jogo()
        self.papel_jogador = 1
        self.tesoura_jogador = 0
        self.pedra_jogador = 0

    def mostra_tesoura(self):
        self.usuario.setPixmap(QtGui.QPixmap('img/interface/tesoura.png'))
        self.jogo()
        self.papel_jogador = 0
        self.tesoura_jogador = 1
        self.pedra_jogador = 0

    def mostra_pedra(self):
        self.usuario.setPixmap(QtGui.QPixmap('img/interface/pedra.png'))
        self.jogo()
        self.papel_jogador = 0
        self.tesoura_jogador = 0
        self.pedra_jogador = 1

    def jogo(self):
        self.escolha_computador = random.randint(1, 3)
        if self.escolha_computador == 1:
            self.computador.setPixmap(QtGui.QPixmap('img/interface/papel.png'))
            self.papel_computador = 1
        elif self.escolha_computador == 2:
            self.computador.setPixmap(QtGui.QPixmap('img/interface/tesoura.png'))
            self.tesoura_computador = 2
        elif self.escolha_computador == 3:
            self.computador.setPixmap(QtGui.QPixmap('img/interface/pedra.png'))
            self.pedra_computador = 3

        if self.pedra_computador == self.pedra_jogador:
            print('empate')


if __name__ == '__main__':
    aplicacao = QApplication(sys.argv)
    j = JokenPo()
    sys.exit(aplicacao.exec())
