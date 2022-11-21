import random
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip, QLabel
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

        lista_jog_computador = [1, 2, 3]
        opcao_computador = random.randint(1, 3)

        if opcao_computador == 1:
            self.pedra_computador = QLabel(self)
            self.pedra_computador.move(50, 300)
            self.pedra_computador.resize(300, 300)
            self.pedra_computador.setPixmap(QtGui.QPixmap('pedra.jpg'))

        self.imagem_pedra = QLabel(self)
        self.imagem_pedra.move(50, 300)
        self.imagem_pedra.resize(300, 300)
        self.imagem_pedra.setPixmap(QtGui.QPixmap('pedra.jpg'))

        botaoPedra = QPushButton('Pedra', self)
        botaoPedra.move(50, 610)
        botaoPedra.resize(210, 50)
        botaoPedra.setStyleSheet('QPushButton {font:bold; font-size: 20px}')
        # botaoPedra.clicked.connect(self.)
        # background - color:  # 0EB328;

        self.imagem_papel = QLabel(self)
        self.imagem_papel.move(350, 300)
        self.imagem_papel.resize(300, 300)
        self.imagem_papel.setPixmap(QtGui.QPixmap('papel.jpg'))

        botaoPapel = QPushButton('Papel', self)
        botaoPapel.move(350, 610)
        botaoPapel.resize(210, 50)
        botaoPapel.setStyleSheet('QPushButton {font:bold; font-size: 20px}')

        self.imagem_tesoura = QLabel(self)
        self.imagem_tesoura.move(650, 300)
        self.imagem_tesoura.resize(300, 300)
        self.imagem_tesoura.setPixmap(QtGui.QPixmap('tesoura.jpg'))

        botaoTesoura = QPushButton('Tesoura', self)
        botaoTesoura.move(650, 610)
        botaoTesoura.resize(210, 50)
        botaoTesoura.setStyleSheet('QPushButton {font:bold; font-size: 20px}')


        self.CarregandoJanela()

    def CarregandoJanela(self):
        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
        self.setWindowTitle(self.titulo)
        self.show()


    
if __name__ == '__main__':
    aplicacao = QApplication(sys.argv)
    j = Janela()
    sys.exit(aplicacao.exec_())
    