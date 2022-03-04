import sqlite3

from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QWidget, QApplication, QListWidgetItem, QMessageBox
from PyQt5.uic import loadUi
from contactpage import Contact
from aboutapp import AboutApp
import sys

class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        loadUi("main.ui", self)
        self.setFixedSize(900, 514)
        self.setWindowIcon(QtGui.QIcon("assets/images/logo.png"))

        # Signal
        self.calendarWidget.selectionChanged.connect(self.calendarDateChanged)
        self.calendarDateChanged()
        self.saveButton.clicked.connect(self.saveChanges)
        self.addButton.clicked.connect(self.addNewTask)
        self.contactButton.clicked.connect(self.contactpage)
        self.aboutButton.clicked.connect(self.aboutpage)

    # Change Display Task yesterday or after
    def calendarDateChanged(self):
        print("The calendar date was changed.")
        dateSelected = self.calendarWidget.selectedDate().toPyDate()
        print("Date selected:", dateSelected)
        self.updateTaskList(dateSelected)

    # Display Task on Taskslistwidget
    def updateTaskList(self, date):
        self.tasksListWidget.clear()

        db = sqlite3.connect("data.db")
        cursor = db.cursor()
        query = "SELECT task, completed FROM tasks WHERE date = ?"
        row = (date,)
        results = cursor.execute(query, row).fetchall()

        for result in results:
            item = QListWidgetItem(str(result[0]))
            item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
            if result[1] == "YES":
                item.setCheckState(QtCore.Qt.Checked)
            elif result[1] == "NO":
                item.setCheckState(QtCore.Qt.Unchecked)
            self.tasksListWidget.addItem(item)

    def saveChanges(self):
        db = sqlite3.connect("data.db")
        cursor = db.cursor()
        date = self.calendarWidget.selectedDate().toPyDate()

        for i in range(self.tasksListWidget.count()):
            item = self.tasksListWidget.item(i)
            task = item.text()
            if item.checkState() == QtCore.Qt.Checked:
                date = self.calendarWidget.selectedDate().toPyDate()
                query = "DELETE from tasks WHERE task = ? AND date = ? "
                QMessageBox.information(self, "Notice", "Clear Task complete")

            else:
                query = "UPDATE tasks SET completed = 'NO' WHERE task = ? AND date = ?"

            row = (task, date,)
            cursor.execute(query, row).fetchone()
        QMessageBox.information(self, "Notice", "Save Task Success.")
        db.commit()
        self.updateTaskList(date)

    # Add task on tasklist widget
    def addNewTask(self):
        self.tasksListWidget.clear()

        db = sqlite3.connect("data.db")
        cursor = db.cursor()

        newTask = str(self.taskLineEdit.text())
        if len(newTask) == 0:
            date = self.calendarWidget.selectedDate().toPyDate()
            QMessageBox.warning(self,"Notice","Error! You want input something.")
            self.updateTaskList(date)
        else:
            date = self.calendarWidget.selectedDate().toPyDate()

            query = "INSERT INTO tasks(task, completed, date) VALUES (?,?,?)"
            row = (newTask, "NO", date,)

            cursor.execute(query, row)
            db.commit()
            self.updateTaskList(date)
            self.taskLineEdit.clear()

    def contactpage(self):
        self.contact = Contact()
        self.contact.show()

    def aboutpage(self):
        self.aboutpage = AboutApp()
        self.aboutpage.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())


