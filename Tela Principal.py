import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PyQt5 import QtGui
from jogoVelha import *

class Principal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.topo = 200
        self.esquerda = 530
        self.largura = 800
        self.altura = 600

        self.fundo = QLabel(self)
        self.fundo.move(0, 0) # esquerda e do topo
        self.fundo.resize(800, 600) # largura e altura do botão
        self.fundo.setPixmap(QtGui.QPixmap('img/interface/tela inicial.jpg'))
        self.fundo.setScaledContents(True)

        self.botao_jokenpo = QPushButton(self)
        self.botao_jokenpo.move(49, 230)
        self.botao_jokenpo.resize(190, 60)
        self.botao_jokenpo.setFlat(True)

        self.botao_memoria = QPushButton(self)
        self.botao_memoria.move(49, 290)
        self.botao_memoria.resize(190, 60)
        self.botao_memoria.setFlat(True)

        self.botao_forca = QPushButton(self)
        self.botao_forca.move(49, 350)
        self.botao_forca.resize(190, 60)
        self.botao_forca.setFlat(True)

        self.botao_velha = QPushButton(self)
        self.botao_velha.move(49, 420)
        self.botao_velha.resize(190, 60)
        self.botao_velha.setFlat(True)
        self.botao_velha.clicked.connect(self.chamar_segunda_tela)

        self.carregar_janela()

    def chamar_segunda_tela(self):
        velha.show()
        self.hide()

    def carregar_janela(self):
        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
        self.show()

# stylesheet = """
#         Janela {
#             background-image: url('img/interface/tela inicial.jpg');
#             background-repeat: no-repeat;
#             background-position: center;
#             background-color: white;
#         }
# """


if __name__ == '__main__':
    aplicacao = QApplication(sys.argv)
    j = Principal()
    velha = Velha()
    # aplicacao.setStyleSheet(stylesheet)
    sys.exit(aplicacao.exec())
