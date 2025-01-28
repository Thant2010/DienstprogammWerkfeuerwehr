from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMessageBox

from utilityClasses.ShadowEffect import ShadowEffect


def MyMessageBox(windowTitle, message):
    msg = QMessageBox()
    msg.setWindowTitle(windowTitle)
    msg.setWindowIcon(QIcon("icons/windowIcon.ico"))
    msg.setIcon(QMessageBox.Icon.Information)
    msg.setText(message)
    msg.setGraphicsEffect(ShadowEffect().shadow)
    msg.setStandardButtons(QMessageBox.StandardButton.Ok)
    msg.setGeometry(650, 450, 300, 300)

    returnvalue = msg.exec()

    if returnvalue == QMessageBox.StandardButton.Ok:
        pass
