import sys
from PySide6.QtWidgets import QApplication, QWidget, QGridLayout, QLineEdit, QPushButton
from PySide6 import QtCore, QtGui
from PySide6.QtCore import Qt, QEvent
from PySide6.QtGui import QFont, QKeyEvent
from functools import partial

class Calculator(QWidget):
    BUTTONS = { 
                "E": (1, 0, 1, 1),
                "\u25C0": (1, 1, 1, 1),
                "=": (5, 3, 1, 1),
                "x": (1, 3, 1, 1),
                "+": (4, 3, 1, 1),
                "/": (2, 3, 1, 1),
                "-": (3, 3, 1, 1),
                "7": (2, 0, 1, 1),
                "8": (2, 1, 1, 1),
                "9": (2, 2, 1, 1),
                "4": (3, 0, 1, 1),
                "5": (3, 1, 1, 1),
                "6": (3, 2, 1, 1),
                "1": (4, 0, 1, 1),
                "2": (4, 1, 1, 1),
                "3": (4, 2, 1, 1),
                "0": (5, 0, 1, 2),
                ".": (5, 2, 1, 1),
    }
    dict_btn = {}
    btn_valides = {'0','1','2','3','4','5','6','7','8','9','E','e','\u25C0', '.', '+','-','*','x','/', '='}
    btn_operateurs = {'+','-','*','x','/'}

    def __init__(self):
        super().__init__()

        self.ecran = ''
        self.setWindowTitle('Calculatrice')
        self.setFixedSize(220,220)
        self.setup_ui()
        self.setup_colors()
        #
        # Connections
        #
        i = 0
        for label, object in self.dict_btn.items():
            self.dict_btn[label].clicked.connect(partial(self.press, label))
            i += 1

    def keyPressEvent(self, e: QtGui.QKeyEvent) -> None:
        super().keyPressEvent(e)
        label = e.text()
        if (e.key() == Qt.Key_Return) or (e.key() == Qt.Key_Enter):
            label = "="
        elif(e.key() == Qt.Key_Backspace):
            label = "\u25C0"

        self.press(label)

        return

    def is_valid(self, label):
        return label in self.btn_valides

    def press(self, label):

        self.ecran = self.result_ecran.text()

        if (label == "E") or (label == "e"):
            self.ecran = '0'
            label = ''
        elif label == "\u25C0":
            self.ecran = self.supprime_dernier_caractere(self.ecran)
            label = ''
        elif label in self.btn_operateurs:
            self.ecran = self.ajouter_operateur(label)
        elif label == '=':
            self.ecran = self.calcule()
        else:
            self.ecran = self.ajouter_caractere( label)

        self.result_ecran.setText(self.ecran)

    def calcule(self):
        if self.precedent_operateur():
            return self.ecran
        tmp = self.ecran.replace('x', '*')
        return str(eval(tmp))
        
    def ajouter_operateur(self, label):
        if self.premiere_position():
            return '0'
        if self.precedent_operateur():
            return self.ecran

        tmp = self.ajouter_caractere(label)
        return tmp

    def precedent_operateur(self):
        if self.ecran[-1:] in self.btn_operateurs:
            return True
        return False

    def premiere_position(self):
        return self.ecran == '0'

    def ajouter_caractere(self, label):
        if self.ecran == '0':
            return label
        if self.ecran == '':
            return '0'
        return self.ecran + label 

    def supprime_dernier_caractere(self, ecran):
        ecran = ecran[:-1]
        if ecran == "":
            ecran = '0'
        return ecran

    def setup_ui(self):

        layout = QGridLayout(self)
        
        self.result_ecran = QLineEdit()
        self.result_ecran.setText('0')
        self.result_ecran.setEnabled(False)
        self.result_ecran.setAlignment(Qt.AlignRight)
        self.result_ecran.setFont(QFont('Arial', 16))
        self.result_ecran.setFocusPolicy(Qt.StrongFocus)
        self.result_ecran.setFocus()
        layout.addWidget(self.result_ecran, 0,0,1,4)

        for label, position in self.BUTTONS.items():
            btn = QPushButton(label)
            layout.addWidget(btn, *position)
            self.dict_btn[label] = btn
        btn.setFocus() # évite que que le focus initial soit sur l'effacement (pb du key_space !)

    def setup_colors(self):
        self.setStyleSheet("background-color: #5C3D37")
        self.result_ecran.setStyleSheet("background-color:#756C6A; color:white")
        i = 0
        for label, object in self.dict_btn.items():
            self.dict_btn[label].setFont(QFont('Arial', 14))
            if i < 2:
                self.dict_btn[label].setStyleSheet("background-color:#F52D2A")
            elif i < 7:
                self.dict_btn[label].setStyleSheet("background-color:#A87065;font-size:18")
            else:
                self.dict_btn[label].setStyleSheet("background-color:#F5A494")
            i += 1



#=======================================#
#                  Main                 #
#=======================================#
app = QApplication(sys.argv)
win = Calculator()
win.show()

app.exec()
