from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMessageBox

from utilityClasses.shadowEffect import ShadowEffect


class CustomMessageBox(QMessageBox):

    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon("icons/windowIcon.ico"))
        self.setFixedSize(300, 300)
        self.setGraphicsEffect(ShadowEffect().shadow)

    def showInfoMessage(self, windowTitle, message):

        self.setWindowTitle(windowTitle)
        self.setIcon(QMessageBox.Icon.Information)
        self.setText(message)
        self.setStandardButtons(QMessageBox.StandardButton.Ok)

        return self.exec()

    def showYesNoMessage(self, windowTitle, message):
        self.setWindowTitle(windowTitle)
        self.setIcon(QMessageBox.Icon.Question)
        self.setText(message)
        self.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

        return self.exec()