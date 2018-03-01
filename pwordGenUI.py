import random
from pwordGen import pwordGenn
from PyQt5 import QtWidgets, QtGui
import sys

class Pencere(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def generate(self,digits):
        result = pwordGenn(digits)

        self.label_2.setText("Şifreniz: " + result)

    def init_ui(self):

        self.label_1 = QtWidgets.QLabel("Kaç Haneli Bir Şifre Üretmek İstediğinizi Girin")
        self.buton = QtWidgets.QPushButton("Şifre Üret")
        self.yazi_alani = QtWidgets.QLineEdit()
        self.label_2 = QtWidgets.QLabel("")


        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.label_1)
        v_box.addStretch()
        v_box.addWidget(self.yazi_alani)
        v_box.addWidget(self.label_2)
        v_box.addStretch()
        v_box.addWidget(self.buton)

        self.buton.clicked.connect(lambda x : self.generate(self.yazi_alani.text()))


        self.setLayout(v_box)
        self.setWindowTitle("Şifre Üreticisi")
        self.show()


app = QtWidgets.QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec_())