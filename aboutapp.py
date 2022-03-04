import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi

class AboutApp(QWidget):
    def __init__(self):
        super().__init__()
        loadUi("aboutapp.ui", self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setFixedSize(400, 500)
        self.setWindowIcon(QIcon("assets/images/logo.png"))
        self.Pixmap = QPixmap('assets/images/logo.png')
        self.pixmap = self.Pixmap.scaledToWidth(301)
        self.pixmap = self.Pixmap.scaledToHeight(201)
        self.label.setPixmap(self.pixmap)
        self.label.resize(301,211)

        self.backButton.clicked.connect(self.Backpage)

    def Backpage(self):
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AboutApp()
    window.show()
    sys.exit(app.exec())