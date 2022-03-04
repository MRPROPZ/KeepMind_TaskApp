import sys, time
from PyQt5.QtWidgets import QApplication, QWidget, QProgressBar, QLabel, QFrame, QVBoxLayout
from PyQt5.QtCore import Qt, QTimer
from secondpage import Window


class SplashScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1100, 500)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self._counter = 0
        self._n = 100  # total instance

        self.initUI()

        self.timer = QTimer()
        self.timer.timeout.connect(self.loading)
        self.timer.start(30)

    def initUI(self):
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.frame = QFrame()
        self.frame.setStyleSheet("background-color: #2F4454;")
        layout.addWidget(self.frame)

        self.labelTitle = QLabel(self.frame)

        # center labels
        self.labelTitle.resize(self.width() - 10, 150)
        self.labelTitle.move(0, 40)  # x, y
        self.labelTitle.setText('KeepMind App')
        self.labelTitle.setAlignment(Qt.AlignCenter)
        self.labelTitle.setStyleSheet("font-size: 60px;color: #93deed;")

        self.labelDescription = QLabel(self.frame)
        self.labelDescription.resize(self.width() - 10, 50)
        self.labelDescription.move(0, self.labelTitle.height())
        self.labelDescription.setText('<strong>Loading App...</strong>')
        self.labelDescription.setAlignment(Qt.AlignCenter)
        self.labelDescription.setStyleSheet("font-size: 30px;color: #c2ced1;")

        self.progressBar = QProgressBar(self.frame)
        self.progressBar.resize(self.width() - 200 - 10, 50)
        self.progressBar.move(100, self.labelDescription.y() + 130)
        self.progressBar.setAlignment(Qt.AlignCenter)
        self.progressBar.setRange(0, self._n)
        self.progressBar.setStyleSheet("text-align: center;")

        self.labelLoading = QLabel(self.frame)
        self.labelLoading.resize(self.width() - 10, 50)
        self.labelLoading.move(0, self.progressBar.y() + 70)
        self.labelLoading.setAlignment(Qt.AlignCenter)
        self.labelLoading.setText('loading...')
        self.labelLoading.setStyleSheet("font-size: 30px;color: #e8e8eb;")

    def loading(self):
        self.progressBar.setValue(self._counter)

        # counter = 30
        if self._counter == int(self._n * 0.3):
            self.labelDescription.setText('<strong>Loading database...</strong>')
        # counter = 60
        elif self._counter == int(self._n * 0.6):
            self.labelDescription.setText('<strong>Nearly Success...</strong>')
        # counter = 90
        elif self._counter == int(self._n * 0.9):
            self.labelDescription.setText('<strong>Loading Success...</strong>')
        # counter = 100
        elif self._counter >= self._n:
            self.timer.stop()
            self.close()

            time.sleep(1)

            ## => Open Application
            self.myapp = Window()
            self.myapp.show()

        self._counter += 1


if __name__ == '__main__':

    app = QApplication(sys.argv)
    splash = SplashScreen()
    splash.show()

    try:
        sys.exit(app.exec_())
    except SystemExit:
        print('Closing Window...')

