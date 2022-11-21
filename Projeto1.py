import sys
from PyQt5.QtWidgets import QApplication, QMainWindow # para criar uma janela
from PyQt5.QtWidgets import QPushButton, QToolTip # para criar um botão e mudar a dor dele
from PyQt5.QtWidgets import QLabel # para criar um label
from PyQt5 import QtGui # módulo para trabalhar com imagens
from PyQt5.QtWidgets import QLineEdit # para adicionar a caixa de texto
from PyQt5.QtCore import QTimer

# LABEL = Rótulo para mostrar uma informação para o usuário

# Herança
class Janela1(QMainWindow):
    def __init__(self):
        super().__init__()

        self.topo =200 # altura que a janela vai aparecer na tela. distância que ela vai ficar no computador
        self.esquerda =530 # distância que vai ficar da tela para o lado esquerdo
        self.largura = 800 # tamanho da janela
        self.altura =600 # tamanho da janela
        self.titulo ="Primeira janela"

        self.caixa_texto = QLineEdit(self)
        self.caixa_texto.move(25, 90)
        self.caixa_texto.resize(250, 50)

        botao1 = QPushButton('Botao 1', self) # instanciando a classe, dando um nome para o botao
        botao1.move(100, 250) # posicao que quer que o botao apareça DENTRO DA JANELA. Pega a posição da esquerda e do topo
        botao1.resize(150, 80) # largura e altura do botão
        botao1.setStyleSheet('QPushButton {background-color: #0EB328; font:bold; font-size: 20px}') # método responsável pelo style do botão
        botao1.clicked.connect(self.botao1_click) # método associado ao click do botão usando um método ppronto da classe.

        botao2 = QPushButton('Botao 2', self)
        botao2.move(300, 250)
        botao2.resize(150, 80)
        botao2.setStyleSheet('QPushButton {background-color: #B21628; font: bold; font-size: 20px}')
        botao2.clicked.connect(self.botao2_click)

        botao_leitura = QPushButton('Enviar texto', self)
        botao_leitura.move(500, 250)
        botao_leitura.resize(150, 80)
        botao_leitura.setStyleSheet('QPushButton {background-color: #0EB328; font:bold; font-size: 20px}')
        botao_leitura.clicked.connect(self.leitura)

        self.label_1 = QLabel(self)
        self.label_1.setText("Aperte um botão:")
        self.label_1.move(330, 180)
        self.label_1.setStyleSheet('QLabel {font: bold; font-size: 20px; color: #000000}')
        self.label_1.resize(200, 60)

        self.imagem = QLabel(self)
        self.imagem.move(278, 350)
        # self.imagem.setPixmap(QtGui.QPixmap('sol.png'))
        self.imagem.resize(200, 200)
        self.imagem.setScaledContents(True)

        self.label_caixa = QLabel(self)
        self.label_caixa.setText("Digitou: ")
        self.label_caixa.move(530, 180)
        self.label_caixa.setStyleSheet('QLabel {font: bold; font-size: 20px; color: #000000}')
        self.label_caixa.resize(200, 60)

        self.timer = QTimer()
        self.timer.timeout.connect(self.timeout)

        # tem que criar o botão e a label antes de chamar a tela para o programa consegui ler o código antes
        self.CarregandoJanela() # chamando o método SHOW dentro da classe

    def timeout(self):
        self.label_1.setText("MUITO OBRIGADA!")

    def botao1_click(self):
        print('O botão 1 foi clicado.')
        self.label_1.setText("LIGADO")
        self.label_1.setStyleSheet('QLabel {font: bold; font-size: 20px; color: #007F00}')
        self.imagem.setPixmap(QtGui.QPixmap('sol.png')) # método que define a imagem vai aparecer

    def botao2_click(self):
        print('O botão 2 foi clicado.')
        self.label_1.setText("DESLIGADO")
        self.label_1.setStyleSheet('QLabel {font: bold; font-size: 20px; color: #B21628}')
        self.imagem.setPixmap(QtGui.QPixmap('lua.png')) # método que define a imagem vai aparecer

    def leitura(self):
        conteudo = self.caixa_texto.text()
        self.label_caixa.setText("Digitou: "+conteudo)
        if self.timer.isActive() == False:
            self.timer.start(5000)

    def CarregandoJanela(self): # vai ser usado os métodos que já existem na classe QMainWindow
        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura) # chamando o método para criar a janela
        self.setWindowTitle(self.titulo) # chamando o método para colocar o título
        self.show() # método para mostrar a janela

if __name__ == '__main__':
    # APLICACAO = é a criação de um OBJETO
    aplicacao = QApplication(sys.argv) # Para poder mexer nos parâmetros do sistema responsável por fechar a janela e coisas relacionadas
    j1 = Janela1() # objeto com a instância da classe janela
    sys.exit(aplicacao.exec_()) # para sair do programa em execução quando fechar a atela
