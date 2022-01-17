import sys
from PySide6.QtWidgets import QApplication, QWidget, QGridLayout, QLineEdit, QPushButton, QVBoxLayout
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from functools import partial

class Calculator(QWidget):

    BUTTONS = { 
                "C": (1, 0, 1, 1),
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

    def __init__(self):
        super().__init__()

        self.setWindowTitle('Calculatrice')
        self.setFixedSize(220,220)
        self.setup_ui()
        self.setup_colors()
        #
        # Connections
        #
        i = 0
        for label, oject in self.dict_btn.items():
            if True: #i > 2:
                self.dict_btn[label].clicked.connect(partial(self.press, label))
            i += 1

    def press(self, label ):
        if label == "C":
            self.result_screen.setText('0')
            return
        screen = self.result_screen.text()
        if label == "\u25C0":
            screen = screen[:-1]
            label = ''
            if screen == '':
                self.result_screen.setText('0')
                return
        if screen == "0":
            screen = ''
        screen = screen + label
        print(screen)
        self.result_screen.setText(screen)

    def setup_ui(self):

        layout = QGridLayout(self)
        
        self.result_screen = QLineEdit()
        self.result_screen.setText('0')
        self.result_screen.setAlignment(Qt.AlignRight)
        self.result_screen.setFont(QFont('Arial', 16))
        layout.addWidget(self.result_screen, 0,0,1,4)

        for label, position in self.BUTTONS.items():
            btn = QPushButton(label)
            layout.addWidget(btn, *position)
            self.dict_btn[label] = btn

    def setup_colors(self):
        self.setStyleSheet("background-color: #5C3D37")
        self.result_screen.setStyleSheet("background-color:#756C6A")
        i = 0
        for label, object in self.dict_btn.items():
            if i < 2:
                self.dict_btn[label].setStyleSheet("background-color:#F52D2A")
            elif i < 7:
                self.dict_btn[label].setStyleSheet("background-color:#A87065;font-size:18")
            else:
                self.dict_btn[label].setStyleSheet("background-color:#F5A494")
                self.dict_btn[label].setFont(QFont('Arial', 14))

            i += 1



#=======================================#
#                  Main                 #
#=======================================#
app = QApplication(sys.argv)
win = Calculator()
win.show()

app.exec()
