import random
import sys
import time

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip, QLabel
from PyQt5.QtCore import QTimer
from PyQt5 import QtGui

class Janela(QMainWindow):
    def __init__(self):
        super().__init__()

        self.topo = 200
        self.esquerda = 530
        self.largura = 920
        self.altura = 700
        self.titulo = "JoKenPo"

        self.titulo2 = QLabel(self)
        self.titulo2.setText("JoKenPo")
        self.titulo2.move(350, 20)
        self.titulo2.setStyleSheet('QLabel {font: bold; font-size: 50px; color: #000000}')
        self.titulo2.resize(300, 60)

        self.titulo_computador = QLabel(self)
        self.titulo_computador.setText("Computador:")
        self.titulo_computador.move(20, 150)
        self.titulo_computador.setStyleSheet('QLabel {font: bold; font-size: 20px; color: #000000}')
        self.titulo_computador.resize(300, 60)

        self.titulo_jogador = QLabel(self)
        self.titulo_jogador.setText("Você:")
        self.titulo_jogador.move(600, 150)
        self.titulo_jogador.setStyleSheet('QLabel {font: bold; font-size: 20px; color: #000000}')
        self.titulo_jogador.resize(300, 60)

        self.imagem_computador = QLabel(self)
        self.imagem_computador.move(160, 120)
        self.imagem_computador.resize(150, 150)
        self.imagem_computador.setScaledContents(True)

        self.imagem_jogador = QLabel(self)
        self.imagem_jogador.move(710, 120)
        self.imagem_jogador.resize(150, 150)
        self.imagem_jogador.setScaledContents(True)

        botaoIniciar = QPushButton('Iniciar partida', self)
        botaoIniciar.move(350, 210)
        botaoIniciar.resize(210, 50)
        botaoIniciar.setStyleSheet('QPushButton {font-size: 20px}')
        botaoIniciar.clicked.connect(self.computador)

        self.imagem_pedra = QLabel(self)
        self.imagem_pedra.move(85, 400)
        self.imagem_pedra.resize(150, 150)
        self.imagem_pedra.setPixmap(QtGui.QPixmap('img/pedra.jpg'))
        self.imagem_pedra.setScaledContents(True)

        botaoPedra = QPushButton('Pedra', self)
        botaoPedra.move(50, 610)
        botaoPedra.resize(210, 50)
        botaoPedra.setStyleSheet('QPushButton {font:bold; font-size: 20px}')
        botaoPedra.clicked.connect(self.jogador_pedra)
        # botaoPedra.clicked.connect(self.)
        # background - color:  # 0EB328;

        self.imagem_papel = QLabel(self)
        self.imagem_papel.move(385, 400) #vai p´baixo quanot maior é
        self.imagem_papel.resize(150, 150)
        self.imagem_papel.setPixmap(QtGui.QPixmap('img/papel.jpg'))
        self.imagem_papel.setScaledContents(True)

        botaoPapel = QPushButton('Papel', self)
        botaoPapel.move(350, 610)
        botaoPapel.resize(210, 50)
        botaoPapel.setStyleSheet('QPushButton {font:bold; font-size: 20px}')
        botaoPapel.clicked.connect(self.jogador_papel)

        self.imagem_tesoura = QLabel(self)
        self.imagem_tesoura.move(685, 400)
        self.imagem_tesoura.resize(150, 150)
        self.imagem_tesoura.setPixmap(QtGui.QPixmap('img/tesoura.jpg'))
        self.imagem_tesoura.setScaledContents(True)

        botaoTesoura = QPushButton('Tesoura', self)
        botaoTesoura.move(650, 610)
        botaoTesoura.resize(210, 50)
        botaoTesoura.setStyleSheet('QPushButton {font:bold; font-size: 20px}')
        botaoTesoura.clicked.connect(self.jogador_tesoura)

        # self.label_tempo_jogo = QLabel(self)
        # self.label_tempo_jogo.setStyleSheet('QLabel {font: bold; font-size: 20px; color: #000000}')
        # self.label_tempo_jogo.move(530, 180)
        # self.label_tempo_jogo.resize(200, 60)
        #
        self.timer = QTimer()
        self.timer.timeout.connect(self.computador)

        self.CarregandoJanela()

    def timeout(self):
        self.label_tempo_jogo.setText("MUITO OBRIGADA!")


    # def leitura(self):
    #     conteudo = self.caixa_texto.text()
    #     self.label_caixa.setText("Digitou: " + conteudo)
    #     if self.timer.isActive() == False:
    #         self.timer.start(5000)

    def computador(self):
        self.timer.start(1000)
        opcao_computador = random.randint(1, 3)
        print(opcao_computador)
        if opcao_computador == 1:
            self.imagem_computador.setPixmap(QtGui.QPixmap('img/pedra.jpg'))
        elif opcao_computador == 2:
            self.imagem_computador.setPixmap(QtGui.QPixmap('img/papel.jpg'))
        elif opcao_computador == 3:
            self.imagem_computador.setPixmap(QtGui.QPixmap('img/tesoura.jpg'))

    def jogador_pedra(self):
        self.imagem_jogador.setPixmap(QtGui.QPixmap('img/pedra_reverse.jpg'))

    def jogador_papel(self):
        self.imagem_jogador.setPixmap(QtGui.QPixmap('img/papel_reverse.jpg'))

    def jogador_tesoura(self):
        self.imagem_jogador.setPixmap(QtGui.QPixmap('img/tesoura_reverse.jpg'))


    def CarregandoJanela(self):
        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
        self.setWindowTitle(self.titulo)
        self.show()


    
if __name__ == '__main__':
    aplicacao = QApplication(sys.argv)
    j = Janela()
    sys.exit(aplicacao.exec_())
    
