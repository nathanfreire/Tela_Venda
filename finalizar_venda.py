from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox, QHBoxLayout
import sys

class finalizar_venda(QWidget):
    def __init__(self):
        super().__init__()

        # Texto para o título
        self.setWindowTitle("Finalizar Vendas")

        # Geometria da tela
        self.setGeometry(500,300,650,370)

        # Layout Principal
        self.layout_v = QVBoxLayout()
        #-----------------------------------

        # Label de cima
        self.label_cima = QLabel("Finalizar Vendas")
        self.label_cima.setFixedHeight(100)
        self.label_cima.setStyleSheet("QLabel{background-color: #fff; font-weight:bold}")
        #-----------------------------------
        
        # Label do meio 
        self.label_meio = QLabel()
        #self.label_meio.setFixedHeight()
        self.label_meio.setStyleSheet("QLabel{background-color: #000}")

        # Layout 
        self.layout_h = QHBoxLayout()

        #Adicionar o layout na tela
        self.setLayout(self.layout_v)
        self.label_meio.setLayout(self.layout_h)

        # Criar label esquerda
        self.label_esquerda = QLabel()
        # Layout vertical para um ficar do lado do outro
        self.layout_vertical_esquerda = QVBoxLayout()
        # label para guardar o texto total de venta e a caixa total de venda, ira guardar uma nova label e uma lineEdit
        self.label_tudo = QLabel()

        # adicionar a label tudo ao layout_vertical_esquerda
        self.layout_vertical_esquerda.addWidget(self.label_tudo)

        # Criar o layout horizontal para label tudo e lineEdit

        self.layout_h_total_venda = QHBoxLayout()

        self.label_venda = QLabel("Total de Venda")
        
        self.label_tudo.setLayout(self.layout_h_total_venda)
        # adicionar o layout vertical da esquerda na coluna da esquerda
        self.label_esquerda.setLayout(self.layout_vertical_esquerda)

        self.label_esquerda.setStyleSheet("QLabel{background-color: #ffb7d5}")

        

        # label dentro dela criar um layout H

        
        # Criar label direita
        self.label_direita = QLabel()
        self.label_direita.setStyleSheet("QLabel{background-color: #00ffff}")

        # Layout vertical para um ficar do lado do outro
        self.layout_vertical_direita = QVBoxLayout()



        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #-----------------------------------

        # Label do baixo
        self.label_baixo = QLabel()
        self.label_baixo.setFixedHeight(200)
        self.label_baixo.setStyleSheet("QLabel{background-color: #f1e788}")

        # Layout 
        self.layout_h_baixo = QHBoxLayout()

        self.setLayout(self.layout_v)
        self.label_baixo.setLayout(self.layout_h_baixo)

        #-----------------------------------




        

        self.layout_v.addWidget(self.label_cima)
        
        self.layout_v.addWidget(self.label_meio)
        self.layout_h.addWidget(self.label_esquerda)
        self.layout_h.addWidget(self.label_direita)

        self.layout_v.addWidget(self.label_baixo)
        self.layout_h_baixo.addWidget(self.label_baixo)
        

        #Adicionar o layout na tela
        self.setLayout(self.layout_v)

app = QApplication(sys.argv)
cx = finalizar_venda()
cx.show()
app.exec_()        



