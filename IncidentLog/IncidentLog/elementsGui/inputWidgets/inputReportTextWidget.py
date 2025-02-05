from PyQt6.QtWidgets import QTextEdit

from utilityClasses.signalManager import signalManager
from utilityFunctions.myMessageBox import MyMessageBox


class InputReportTextWidget(QTextEdit):

    def __init__(self):
        super().__init__()

        signalManager.on_set_default_values.connect(self.__setDefault)
        signalManager.on_get_change.connect(self.__apendChanges)

        self.setMinimumWidth(400)
        self.setProperty("fontsize", "medium")

    def getInput(self) -> str:
        if self.toPlainText() != "":
            return self.toPlainText()
        else:
            MyMessageBox("Achtung", "Bitte einen Text eingeben")
            self.setFocus()
            return None

    def __setDefault(self):

        self.setText("")

    def __apendChanges(self, newText: str, dateTime: str, user: str):

        self.append(f"Nachtrag: {newText} ({dateTime} durch {user})")
