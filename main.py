from PyQt6 import QtWidgets
from sys import argv, exit

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("Ee")
        self.setGeometry(300, 250, 350, 200)

        self.new_text = QtWidgets.QLabel(self)

        self.main_text = QtWidgets.QLabel(self)
        self.main_text.setText("Йоуfgredfzrdfrg")
        self.main_text.move(100, 100)
        self.main_text.adjustSize()

        self.btn = QtWidgets.QPushButton(self)
        self.btn.move(100, 125)
        self.btn.setText('ЯДЕРНАЯ КНОПКА')
        self.btn.adjustSize()
        self.btn.clicked.connect(self.add_label)


    def add_label(self):
        self.new_text.setText("Shat EEEEEEEE")
        self.new_text.move(100, 50)
        self.new_text.adjustSize()

def application():
    app = QtWidgets.QApplication(argv)
    window = Window()

    window.show()
    exit(app.exec())
application()