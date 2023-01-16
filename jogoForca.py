import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit
from PyQt5 import QtGui


class Forca(QMainWindow):
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
        self.fundo.setPixmap(QtGui.QPixmap('img/interface/forca.jpg'))

        self.botao_avada = QPushButton(self)
        self.botao_avada.move(150, 460)
        self.botao_avada.resize(190, 80)

        self.caixa_texto = QLineEdit(self)
        self.caixa_texto.setStyleSheet('border: 2px solid rgb(52, 59, 72, 20%); border-radius: 5px; background-color: rgb(52, 59, 72, 20%);color: rgb(205, 195, 255);')
        self.caixa_texto.move(120, 325)
        self.caixa_texto.resize(300, 40)

        self.carregar_janela()

    def carregar_janela(self):
        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
        self.show()


if __name__ == '__main__':
    aplicacao = QApplication(sys.argv)
    f = Forca()
    sys.exit(aplicacao.exec())
