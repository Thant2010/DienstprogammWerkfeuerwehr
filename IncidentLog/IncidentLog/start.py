import locale
import os
import sys
import traceback

from PyQt6 import QtGui
from PyQt6.QtWidgets import QApplication

from elementsGui.window import Window
from utilityFunctions.writeErrorToLogFile import writeErrorToLogFile



def exceptionHandler(exc_type, exc_value, exc_tb):
    tb = "\n".join(traceback.format_exception(exc_type, exc_value, exc_tb))
    writeErrorToLogFile(f'{tb}')
    QApplication.quit()


def loadMultipleStylesheets():
    combinedStylesheet = ""
    for filename in os.listdir("styles"):
        if filename.endswith(".qss"):
            file_path = os.path.join("styles", filename)
            with open(file_path, "r") as styleFile:
                combinedStylesheet += styleFile.read() + "\n"
    return combinedStylesheet


if __name__ == "__main__":
    app = QApplication(sys.argv)
    stylesheet = loadMultipleStylesheets()
    app.setStyleSheet(stylesheet)
    app.setStyle("Fusion")
    locale.setlocale(locale.LC_ALL, 'de_DE')
    QtGui.QFontDatabase.addApplicationFont('font/Leoscar Sans Serif.ttf')
    QtGui.QFontDatabase.addApplicationFont('font/Leoscar Serif.ttf')
    QtGui.QFontDatabase.addApplicationFont('font/Orbitron-VariableFont_wght.ttf')

    sys.excepthook = exceptionHandler

    w = Window()
    sys.exit(app.exec())
