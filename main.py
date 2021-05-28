# This Python file uses the following encoding: utf-8
import sys
import os


from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader


class RemoveLineBreaks(QWidget):
    def __init__(self):
        super(RemoveLineBreaks, self).__init__()
        loader = QUiLoader()
        self.ui = loader.load('form.ui')
        self.ui.show()
        self.ui.Submit.clicked.connect(self.submit)
        self.ui.Reset.clicked.connect(self.reset)

    def submit(self):
        temp = self.ui.txt.toPlainText()
        self.ui.txt.setText(temp.replace('\n', ' '))

    def reset(self):
        self.ui.txt.setText('')

if __name__ == "__main__":
    app = QApplication([])
    widget = RemoveLineBreaks()
    sys.exit(app.exec())
