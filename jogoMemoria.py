import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PyQt5 import QtGui

class Memoria(QMainWindow):
    def __init__(self):
        super().__init__()
        self.topo = 100
        self.esquerda = 100
        self.largura = 1000
        self.altura = 600

        self.fundo = QLabel(self)
        self.fundo.move(0, 0)
        self.fundo.resize(1000, 600)
        self.fundo.setScaledContents(True)
        self.fundo.setPixmap(QtGui.QPixmap('img/interface/velha.jpg'))

        self.carregar_janela()

    def carregar_janela(self):
        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
        self.show()


if __name__ == '__main__':
    aplicacao = QApplication(sys.argv)
    f = Memoria()
    sys.exit(aplicacao.exec())
