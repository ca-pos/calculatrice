import sys
from PySide6.QtWidgets import QApplication, QWidget, QGridLayout, QLineEdit, QPushButton, QVBoxLayout
from PySide6.QtCore import Qt

BUTTONS = { "C": (1, 0, 1, 1),
            "\u25C0": (1, 1, 1, 1),
            "=": (5, 3, 1, 1),
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
            "+": (4, 3, 1, 1),
            "/": (2, 3, 1, 1)
}
class Calculator(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Calculatrice')
        self.setFixedSize(220,220)

        layout = QGridLayout(self)
        
        self.result_screen = QLineEdit()
        self.result_screen.setText('0')
        self.result_screen.setAlignment(Qt.AlignRight)
        layout.addWidget(self.result_screen, 0,0,1,4)
    
        self.dict_btn = {}
        for label, position in BUTTONS.items():
            btn = QPushButton(label)
            layout.addWidget(btn, *position)
            self.dict_btn[label] = btn
        print(self.dict_btn['\u25C0'].text())

app = QApplication(sys.argv)
win = Calculator()
win.show()

app.exec()
