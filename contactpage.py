import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi

class Contact(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setFixedSize(400, 400)
        loadUi("contact.ui", self)
        self.setWindowIcon(QIcon("assets/images/logo.png"))

        self.backButton.clicked.connect(self.Backpage)

    def Backpage(self):
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Contact()
    window.show()
    sys.exit(app.exec())