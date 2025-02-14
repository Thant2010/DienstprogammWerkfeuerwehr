from PyQt6.QtCore import Qt, QDateTime
from PyQt6.QtWidgets import QDateTimeEdit

from utilityClasses.signalManager import signalManager
from utilityClasses.customMessageBox import CustomMessageBox


class InputTimeWidget(QDateTimeEdit):

    def __init__(self, clearValue):
        super().__init__()
        signalManager.on_set_default_values.connect(self.__setClearValue)

        self.setMinimumSize(200, 30)
        self.setDisplayFormat("dd.MM.yyyy HH:mm")
        self.setCalendarPopup(True)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setMaximumDate(QDateTime.currentDateTime().date())

        if clearValue:
            self.__setClearValue()
        else:
            self.setDateTime(QDateTime.currentDateTime())

    def getCurrentValue(self) -> str:
        if self.dateTime().toString("dd.MM.yyyy HH:mm") == "01.01.2000 00:00":
            return None
        if self.dateTime() <= QDateTime.currentDateTime():
            return self.dateTime().toString("dd.MM.yyyy HH:mm")
        else:
            CustomMessageBox().showInfoMessage("Achtung", "Die gewählte Zeit liegt in der Zukunft")
            self.setFocus()
            return None

    def getCurrenTime(self) -> str:
        return self.time().toString("HH:mm")

    def getCurrenDate(self) -> str:
        return self.date().toString("dd.MM.yyyy")

    def setCurrentDateTime(self):
        self.setDisabled(False)
        self.setDateTime(QDateTime.currentDateTime())

    def __setClearValue(self):
        self.setDisabled(True)
        self.setDateTime(QDateTime(0000, 00, 00, 00, 00))