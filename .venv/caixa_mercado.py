from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout,QMessageBox
import sys 

class CaixaMercado(QWidget):
    def __init__(self):
        super().__init__()

        # Vamos configurar a geometria da tela. Setandos valores de posição X e Y,
        # além de largura e altura
        self.setGeometry(500,30,600,800)

        # Texto para a barra de título
        self.setWindowTitle("Caixa")

        #Layout vertical da tela inteira
        self.layout_v_total = QVBoxLayout()

        #Label titulo
        self.label_titulo = QLabel("Finalizar Venda")
        self.label_titulo.setFixedHeight(100)
        self.label_titulo.setStyleSheet("QLabel{background-color: #fff; font-weight:bold}")
        # adicionar a label de titulo ao layout
        self.layout_v_total.addWidget(self.label_titulo)

        #Label dados
        self.label_dados = QLabel()

        # Criar e adicionar um layout horizontal para 
        # os dados da compra
        self.layout_h_dados = QHBoxLayout()

        #================== Inicio da ESquerda ========================
        # criar label da esquerda ######################################
        self.label_esquerda = QLabel()
        # Criar um layout vertical
        self.layout_v_esquerda = QVBoxLayout()
        # label para guardar o texto Total de venda
        # e a caixa total de venda, ou seja, irá
        # a guardar uma nova label e uma lineEdit
       
    #    ===================Total Venda==============================
       
        self.label_total_venda = QLabel()

        # Criar o layout horizontal para a label total_venda e a 
        # Line Edit
        self.layout_h_total_venda = QHBoxLayout()

        # Criar a label que terá o texto Total de vendas
        self.label_venda = QLabel("Total de Venda:")
        # Criar a LineEdit que recebe o total de venda
        self.edit_venda = QLineEdit("R$ 0,00")
        # adicionar a label_venda e a edit_venda ao layout horizontal venda
        self.layout_h_total_venda.addWidget(self.label_venda)
        self.layout_h_total_venda.addWidget(self.edit_venda)

        # Adiconar o layout_h_total_venda a label _total_venda
        self.label_total_venda.setLayout(self.layout_h_total_venda)

        # adicionar a label_total_venda ao layout_v_esquerda
        self.layout_v_esquerda.addWidget(self.label_total_venda)

# ================== Fim do total venda ======================================


# =================== Inicio do Desconto ====================================

        self.label_desconto = QLabel()

        # Criar o layout horizontal para a label desconto e a 
        # Line Edit
        self.layout_h_desconto = QHBoxLayout()

        # Criar a label que terá o texto Desconto
        self.label_desc = QLabel("Desconto:")
        # Criar a LineEdit que recebe o total de desc
        self.edit_desc = QLineEdit("R$ 0,00")
        # adicionar a label_desc e a edit_desc ao layout horizontal desc
        self.layout_h_desconto.addWidget(self.label_desc)
        self.layout_h_desconto.addWidget(self.edit_desc)

        # Adiconar o layout_h_desconto a label _desconto
        self.label_desconto.setLayout(self.layout_h_desconto)

        # adicionar a label_desconto ao layout_v_esquerda
        self.layout_v_esquerda.addWidget(self.label_desconto)

# =================== Fim do Desconto =========================================


# =================== Inicio do Acréscimo ====================================
        
        self.label_desconto = QLabel()

        # Criar o layout horizontal para a label desconto e a 
        # Line Edit
        self.layout_h_desconto = QHBoxLayout()

        # Criar a label que terá o texto Desconto
        self.label_desc = QLabel("Acréscimo:")
        # Criar a LineEdit que recebe o total de desc
        self.edit_desc = QLineEdit("R$ 0,00")
        # adicionar a label_desc e a edit_desc ao layout horizontal desc
        self.layout_h_desconto.addWidget(self.label_desc)
        self.layout_h_desconto.addWidget(self.edit_desc)

        # Adiconar o layout_h_desconto a label _desconto
        self.label_desconto.setLayout(self.layout_h_desconto)

        # adicionar a label_desconto ao layout_v_esquerda
        self.layout_v_esquerda.addWidget(self.label_desconto)

# =================== Fim do Acréscimo =========================================

# =================== Inicio do Total Líquido ====================================
        
        self.label_desconto = QLabel()

        # Criar o layout horizontal para a label desconto e a 
        # Line Edit
        self.layout_h_desconto = QHBoxLayout()

        # Criar a label que terá o texto Desconto
        self.label_desc = QLabel("Total Líquido:")
        # Criar a LineEdit que recebe o total de desc
        self.edit_desc = QLineEdit("R$ 100,00")
        # adicionar a label_desc e a edit_desc ao layout horizontal desc
        self.layout_h_desconto.addWidget(self.label_desc)
        self.layout_h_desconto.addWidget(self.edit_desc)

        # Adiconar o layout_h_desconto a label _desconto
        self.label_desconto.setLayout(self.layout_h_desconto)

        # adicionar a label_desconto ao layout_v_esquerda
        self.layout_v_esquerda.addWidget(self.label_desconto)

# =================== Fim do Total Líquido =========================================

# =================== Fim do Acréscimo =========================================

        self.label_desconto = QLabel()

        # Criar o layout horizontal para a label desconto e a 
        # Line Edit
        self.layout_h_desconto = QHBoxLayout()

        # Criar a label que terá o texto Desconto
        self.label_desc = QLabel("Troco:")
        # Criar a LineEdit que recebe o total de desc
        self.edit_desc = QLineEdit("R$ 0,00")
        # adicionar a label_desc e a edit_desc ao layout horizontal desc
        self.layout_h_desconto.addWidget(self.label_desc)
        self.layout_h_desconto.addWidget(self.edit_desc)

        # Adiconar o layout_h_desconto a label _desconto
        self.label_desconto.setLayout(self.layout_h_desconto)

        # adicionar a label_desconto ao layout_v_esquerda
        self.layout_v_esquerda.addWidget(self.label_desconto)

# =================== Fim do Total Líquido =========================================


        # Adicionar o layout vertical da esquerda
        # na coluna da esquerda
        self.label_esquerda.setLayout(self.layout_v_esquerda)

        self.label_esquerda.setStyleSheet("QLabel{background-color:gray}")
        # adicionar a label da esquerda no layout 
        # horizontal
        self.layout_h_dados.addWidget(self.label_esquerda)
        #=============================================================

#===================== Fim da Esquerda ========================================

         # criar label da direita
        self.label_direita = QLabel()
        self.layout_v_direita = QVBoxLayout()
        
        self.label_direita.setStyleSheet("QLabel{background-color:yellow}")
        # adicionar a label da direita no layout 
        # horizontal
        
        
        #    =================== Cliente ==============================
        
        self.label_cliente = QLabel()

        # Criar o layout horizontal para a label total_venda e a 
        # Line Edit
        self.layout_h_cliente = QHBoxLayout()

        # Criar a label que terá o texto Total de vendas
        self.label_clien = QLabel("Cliente:")
        # Criar a LineEdit que recebe o total de venda
        self.edit_clien = QLineEdit("1 - CONSUMIDOR FINAL")
        # adicionar a label_venda e a edit_venda ao layout horizontal venda
        self.layout_h_cliente.addWidget(self.label_clien)
        self.layout_h_cliente.addWidget(self.edit_clien)

        # Adiconar o layout_h_total_venda a label _total_venda
        self.label_cliente.setLayout(self.layout_h_cliente)

        # adicionar a label_total_venda ao layout_v_esquerda
        self.layout_v_direita.addWidget(self.label_cliente)

        #    =================== Fim do Cliente ==============================
       

        # Adicionar o layout vertical da esquerda
        # na coluna da esquerda
        self.label_direita.setLayout(self.layout_v_direita)

        self.label_direita.setStyleSheet("QLabel{background-color:yellow}")
        # adicionar a label da direita no layout 
        # horizontal

       

        






        self.layout_h_dados.addWidget(self.label_direita)  
        self.label_dados.setLayout(self.layout_h_dados)
        self.label_dados.setStyleSheet("QLabel{background-color:red}")
        self.layout_v_total.addWidget(self.label_dados)
        
        









        #Label rodape
        self.label_rodape = QLabel()
        # criar um leyout H
        
        self.label_rodape.setFixedHeight(200)
        self.label_rodape.setStyleSheet("QLabel{background-color:white;}")
        self.layout_v_total.addWidget(self.label_rodape)

        # adicionar o layout vertical a tela
        self.setLayout(self.layout_v_total)

        self.layout_h_rodape = QHBoxLayout()

        



        #Label 1
        self.label1 = QLabel()
        self.label1.setStyleSheet("QLabel{background-color:white;}")
        self.layout_v_sair = QVBoxLayout()
        self.btn_sair = QPushButton("(Esc) Sair")
        self.layout_v_sair.addWidget(self.btn_sair)
        self.label1.setLayout(self.layout_v_sair)


        self.layout_h_rodape.addWidget(self.label1)


        




        #Label 2
        self.label2 = QLabel()
        self.label2.setStyleSheet("QLabel{background-color:white;}")
        self.layout_v_cupom = QVBoxLayout()
        
        self.button_text = QLabel("Selecione o Documento para Emissão:")
        
        self.btn_cupom = QPushButton("(F6) Cupom Fiscal")

        self.btn_nfc = QPushButton("(F8) NFC-e OnLine")
        
        self.layout_v_cupom.addWidget(self.button_text)
        self.layout_v_cupom.addWidget(self.btn_cupom)
        self.layout_v_cupom.addWidget(self.btn_nfc)
        self.label2.setLayout(self.layout_v_cupom)


        self.layout_h_rodape.addWidget(self.label2)







        #Label 3
        self.label3 = QLabel()
        self.label3.setStyleSheet("QLabel{background-color:white;}")

        self.layout_v_pedido = QVBoxLayout()
        self.btn_pedido = QPushButton("(F7) Pedido de Venda")
        self.btn_off = QPushButton("(F9) NFC-e OffLine")

        self.layout_v_pedido.addWidget(self.btn_pedido)
        self.layout_v_pedido.addWidget(self.btn_off)

        self.label3.setLayout(self.layout_v_pedido)








        self.layout_h_rodape.addWidget(self.label3)






        self.label_rodape.setLayout(self.layout_h_rodape)












        # Adiconar o layout_h_rodape a label _rodape
        self.label_rodape.setLayout(self.layout_h_rodape)

        # adicionar a label_desconto ao layout_v_esquerda
        self.layout_h_rodape.addWidget(self.label_rodape)


app = QApplication(sys.argv)
tela = CaixaMercado()
tela.show()
app.exec()