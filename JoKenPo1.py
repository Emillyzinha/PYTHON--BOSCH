import random
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip, QLabel
from PyQt5.QtCore import QTimer
from PyQt5 import QtGui


class Janela(QMainWindow):
    def __init__(self):
        super().__init__()

        self.pontos_computador = 0
        self.pontos_jogador = 0
        self.opcao_jogador = 0
        self.contador = 0
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

        self.pontuacao = QLabel(self)
        self.pontuacao.move(600, 20)
        self.pontuacao.setStyleSheet('QLabel {font: bold; font-size: 20px; color: #000000}')
        self.pontuacao.resize(400, 100)

        self.vencedor = QLabel(self)
        self.vencedor.move(10, 20)
        self.vencedor.setStyleSheet('QLabel {font: bold; font-size: 20px; color: #000000}')
        self.vencedor.resize(300, 60)

        self.label_tempo_jogo = QLabel(self)
        self.label_tempo_jogo.setStyleSheet('QLabel {font: bold; font-size: 20px; color: #000000}')
        self.label_tempo_jogo.move(750, 20)
        self.label_tempo_jogo.resize(200, 60)

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

        self.imagem_pedra = QLabel(self)
        self.imagem_pedra.move(85, 400)
        self.imagem_pedra.resize(150, 150)
        self.imagem_pedra.setPixmap(QtGui.QPixmap('img/pedra.jpg'))
        self.imagem_pedra.setScaledContents(True)

        inic = QPushButton('Aperte para iniciar', self)
        inic.move(30, 35)
        inic.resize(210, 50)
        inic.clicked.connect(self.iniciar)

        self.botaoPedra = QPushButton('Pedra', self)
        self.botaoPedra.move(50, 610)
        self.botaoPedra.resize(210, 50)
        self.botaoPedra.setStyleSheet('QPushButton {font:bold; font-size: 20px}')
        self.botaoPedra.clicked.connect(self.jogador_pedra)

        self.imagem_papel = QLabel(self)
        self.imagem_papel.move(385, 400)  # vai p baixo quanto maior é
        self.imagem_papel.resize(150, 150)
        self.imagem_papel.setPixmap(QtGui.QPixmap('img/papel.jpg'))
        self.imagem_papel.setScaledContents(True)

        self.botaoPapel = QPushButton('Papel', self)
        self.botaoPapel.move(350, 610)
        self.botaoPapel.resize(210, 50)
        self.botaoPapel.setStyleSheet('QPushButton {font:bold; font-size: 20px}')
        self.botaoPapel.clicked.connect(self.jogador_papel)

        self.imagem_tesoura = QLabel(self)
        self.imagem_tesoura.move(685, 400)
        self.imagem_tesoura.resize(150, 150)
        self.imagem_tesoura.setPixmap(QtGui.QPixmap('img/tesoura.jpg'))
        self.imagem_tesoura.setScaledContents(True)

        self.botaoTesoura = QPushButton('Tesoura', self)
        self.botaoTesoura.move(650, 610)
        self.botaoTesoura.resize(210, 50)
        self.botaoTesoura.setStyleSheet('QPushButton {font:bold; font-size: 20px}')
        self.botaoTesoura.clicked.connect(self.jogador_tesoura)

        self.timer = QTimer()
        self.timer.timeout.connect(self.computador)

        self.CarregandoJanela()

    def jogador_pedra(self):
        self.imagem_jogador.setPixmap(QtGui.QPixmap('img/pedra_reverse.jpg'))
        self.opcao_jogador = 1

    def jogador_papel(self):
        self.imagem_jogador.setPixmap(QtGui.QPixmap('img/papel_reverse.jpg'))
        self.opcao_jogador = 2

    def jogador_tesoura(self):
        self.imagem_jogador.setPixmap(QtGui.QPixmap('img/tesoura_reverse.jpg'))
        self.opcao_jogador = 3

    def iniciar(self):
        if self.timer.isActive() == False:
            self.contador = 0
            self.botaoPedra.setEnabled(True)
            self.botaoPapel.setEnabled(True)
            self.botaoTesoura.setEnabled(True)
            self.timer.start(1000)

    def computador(self):
        self.opcao_computador = random.randint(1, 3)
        if self.opcao_computador == 1:
            self.imagem_computador.setPixmap(QtGui.QPixmap('img/pedra.jpg'))
        elif self.opcao_computador == 2:
            self.imagem_computador.setPixmap(QtGui.QPixmap('img/papel.jpg'))
        elif self.opcao_computador == 3:
            self.imagem_computador.setPixmap(QtGui.QPixmap('img/tesoura.jpg'))

        if self.opcao_jogador == 0:
            self.pontos_computador += 1
        elif self.opcao_jogador == self.opcao_computador:
            self.pontuacao.setText("Empate")
        elif self.opcao_computador == 1 and self.opcao_jogador == 2:
            self.pontos_jogador += 1
            # print("Computador: ", self.pontos_computador)
        elif self.opcao_computador == 2 and self.opcao_jogador == 3:
            self.pontos_jogador += 1
            # print("Computador: ", self.pontos_computador)
        elif self.opcao_computador == 3 or self.opcao_jogador == 1:
            self.pontos_jogador +=1
            # print("Computador: ", self.pontos_computador)

        elif self.opcao_computador == 2 and self.opcao_jogador == 1:
            self.pontos_computador += 1
            # print("Computador: ", self.pontos_computador)
        elif self.opcao_computador == 3 and self.opcao_jogador == 2:
            self.pontos_computador += 1
            # print("Computador: ", self.pontos_computador)
        elif self.opcao_computador == 1 or self.opcao_jogador == 3:
                self.pontos_computador += 1
                # print("Computador: ", self.pontos_computador)
        self.pontuacao.setText(f"V: {self.pontos_jogador}           C: {self.pontos_computador}")
        self.contador += 1

        if self.contador >= 10:
            self.timer.stop()
            self.botaoPedra.setEnabled(False)
            self.botaoPapel.setEnabled(False)
            self.botaoTesoura.setEnabled(False)
            if self.pontos_jogador > self.pontos_computador:
                self.pontuacao.setText("Jogador venceu com {} pontos".format(self.pontos_jogador))
            elif self.pontos_jogador == self.pontos_computador:
                self.pontuacao.setText("Empate de {} pontos.".format(self.pontos_jogador))
            else:
                self.pontuacao.setText("Computador venceu com {} pontos".format(self.pontos_computador))
        # print(self.contador)
        # print(f"OpçãoC: {self.opcao_computador}")
        # print(f"OpçãoJ: {self.opcao_jogador}")
        self.opcao_jogador = 0

    def CarregandoJanela(self):
        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
        self.setWindowTitle(self.titulo)
        self.show()


if __name__ == '__main__':
    aplicacao = QApplication(sys.argv)
    j = Janela()
    sys.exit(aplicacao.exec_())
