from PyQt6.QtCore import Qt, QDateTime
from PyQt6.QtWidgets import QDateTimeEdit

from utilityClasses.signalManager import signalManager
from utilityFunctions.myMessageBox import MyMessageBox


class InputTimeWidget(QDateTimeEdit):

    def __init__(self):
        super().__init__()
        signalManager.on_set_time_click.connect(lambda: self.setDateTime(QDateTime.currentDateTime()))
        #signalManager.on_set_default_values.connect(lambda: self.setDateTime(QDateTime.currentDateTime()))

        self.setMinimumSize(200, 30)
        self.setDisplayFormat("dd.MM.yyyy HH:mm")
        self.setCalendarPopup(True)
        self.setDateTime(QDateTime.currentDateTime())
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setMaximumDate(QDateTime.currentDateTime().date())

    def getCurrentValue(self) -> str:
        if self.dateTime() <= QDateTime.currentDateTime():
            return self.dateTime().toString("dd.MM.yyyy HH:mm")
        else:
            MyMessageBox("Achtung", "Die gewählte Zeit liegt in der Zukunft")
            self.setFocus()
            return None

    def getCurrenTime(self) -> str:
        return self.time().toString("HH:mm")

    def getCurrenDate(self) -> str:
        return self.date().toString("dd.MM.yyyy")
