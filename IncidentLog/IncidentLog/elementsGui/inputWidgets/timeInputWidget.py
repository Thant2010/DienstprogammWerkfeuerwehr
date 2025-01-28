from PyQt6.QtCore import Qt, QDateTime
from PyQt6.QtWidgets import QDateTimeEdit

from utilityClasses.SignalManager import signalManager


class InputTimeWidget(QDateTimeEdit):

    def __init__(self):
        super().__init__()
        signalManager.on_set_time_click.connect(lambda: self.setDateTime(QDateTime.currentDateTime()))
        self.setMinimumSize(200, 30)
        self.setDisplayFormat("dd.MM.yyyy HH:mm")
        self.setCalendarPopup(True)
        self.setDateTime(QDateTime.currentDateTime())
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setMaximumDate(QDateTime.currentDateTime().date())

    def focusInEvent(self, e):
        self.setSelectedSection(QDateTimeEdit.Section.HourSection)

    def getCurrentValue(self) -> str:
        return self.dateTime().toString("dd.MM.yyyy HH:mm")

    def getCurrenTime(self) -> str:
        return self.time().toString("HH:mm")

    def getCurrenDate(self) -> str:
        return self.date().toString("dd.MM.yyyy")