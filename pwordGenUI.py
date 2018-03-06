import random
from pwordGen import pwordGenn
from PyQt5 import QtWidgets, QtGui
import sys

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def generate(self,digits):
        result = pwordGenn(digits)

        self.label_2.setText("Your password is: " + result +"\nThe generated password is copied to your clipboard.")
        
        cb = app.clipboard() # Create a clipboard object
        cb.setText(result) # Copy the generated password to clipboard

    def init_ui(self):

        self.label_1 = QtWidgets.QLabel("How long would you like your password to be: ")
        self.buton = QtWidgets.QPushButton("GENERATE")
        self.type_space = QtWidgets.QLineEdit()
        self.label_2 = QtWidgets.QLabel("")


        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.label_1)
        v_box.addStretch()
        v_box.addWidget(self.type_space)
        v_box.addWidget(self.label_2)
        v_box.addStretch()
        v_box.addWidget(self.buton)

        self.buton.clicked.connect(lambda x : self.generate(self.type_space.text()))


        self.setLayout(v_box)
        self.setWindowTitle("Python Password Generator")
        self.show()


app = QtWidgets.QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())
