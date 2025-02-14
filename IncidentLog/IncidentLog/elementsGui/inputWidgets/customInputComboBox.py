from PyQt6 import QtCore
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QComboBox

from utilityClasses.signalManager import signalManager
from utilityClasses.customMessageBox import CustomMessageBox


class CustomInputComboBox(QComboBox):

    def __init__(self, comboList: list, readOnly: bool):
        super().__init__()
        signalManager.on_set_default_values.connect(self.__setDefault)


        self.setMinimumSize(200, 30)
        self.setProperty("selectable", True)
        self.setEditable(True)

        self.lineEdit().setReadOnly(readOnly)
        self.lineEdit().setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit().returnPressed.connect(self.__setEntryAlignment)

        self.addItem("---")
        for entry in comboList:
            self.addItem(entry)

        self.__setEntryAlignment()

    def currentText(self):
        if self.currentIndex() != 0:
            return super().currentText()
        else:
            CustomMessageBox().showInfoMessage("Achtung", f"Bitte {self.objectName()} wählen")
            self.setFocus()
            return None

    def __setEntryAlignment(self):
        self.setMaxVisibleItems(self.count())

        for i in range(self.count()):
            index = self.model().index(i, 0)
            self.model().setData(index, QtCore.Qt.AlignmentFlag.AlignCenter, QtCore.Qt.ItemDataRole.TextAlignmentRole)

    def __setDefault(self):
        self.setCurrentIndex(0)

