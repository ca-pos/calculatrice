import sys
from PySide6.QtWidgets import QApplication, QWidget, QGridLayout, QLineEdit, QPushButton, QVBoxLayout

BUTTONS = { "C": (1, 0, 1, 1),
            "E": (1, 1, 1, 1),
            "=": (1, 2, 1, 1),
            "x": (1, 3, 1, 1),
            "7": (2, 0, 1, 1),
            "8": (2, 1, 1, 1),
            "9": (2, 2, 1, 1),
            "4": (3, 0, 1, 1),
            "5": (3, 1, 1, 1),
            "6": (3, 2, 1, 1),
            "-": (3, 3, 1, 1),
            "1": (4, 0, 1, 1),
            "2": (4, 1, 1, 1),
            "3": (4, 2, 1, 1),
            "0": (5, 0, 1, 2),
            ".": (5, 2, 1, 1),
            "+": (5, 3, 2, 1)
}
class Calculator(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Calculatrice')
        self.setFixedSize(220,220)

        layout = QGridLayout(self)
        
        self.result_screen = QLineEdit()

        layout.addWidget(self.result_screen, 0,0,1,4)
    
        # for label, position in BUTTONS.items():
        self.btn = QPushButton("C")
        layout.addWidget(self.btn, 1,0,1,1)
        self.btn = QPushButton("\u25C0")
        layout.addWidget(self.btn, 1,1,1,1)
        self.btn = QPushButton("x")
        layout.addWidget(self.btn, 1,3,1,1)
        self.btn = QPushButton("7")
        layout.addWidget(self.btn, 2,0,1,1)
        self.btn = QPushButton("4")
        layout.addWidget(self.btn, 3,0,1,1)
        self.btn = QPushButton("1")
        layout.addWidget(self.btn, 4,0,1,1)
        self.btn = QPushButton("0")
        layout.addWidget(self.btn, 5,0,1,2)
        self.btn = QPushButton("8")
        layout.addWidget(self.btn, 2,1,1,1)
        self.btn = QPushButton("6")
        layout.addWidget(self.btn, 3,1,1,1)
        self.btn = QPushButton("2")
        layout.addWidget(self.btn, 4,1,1,1)
        self.btn = QPushButton("9")
        layout.addWidget(self.btn, 2,2,1,1)
        self.btn = QPushButton("6")
        layout.addWidget(self.btn, 3,2,1,1)
        self.btn = QPushButton("3")
        layout.addWidget(self.btn, 4,2,1,1)
        self.btn = QPushButton(".")
        layout.addWidget(self.btn, 5,2,1,1)
        self.btn = QPushButton("/")
        layout.addWidget(self.btn, 2,3,1,1)
        self.btn = QPushButton("-")
        layout.addWidget(self.btn, 3,3,1,1)

        # plus_layout = QVBoxLayout()
        # self.btn = QPushButton("+")
        # self.btn.setFixedSize(45,68)
        # plus_layout.addWidget(self.btn)
        # layout.addLayout(plus_layout, 4, 3)


        # self.btn = QPushButton("=")
        # layout.addWidget(self.btn, 1,2,1,1)
        self.btn = QPushButton("=")
        layout.addWidget(self.btn, 5,3,1,1)
        self.btn = QPushButton("+")
        layout.addWidget(self.btn, 4,3, 1, 1)


app = QApplication(sys.argv)
win = Calculator()
win.show()

app.exec()
