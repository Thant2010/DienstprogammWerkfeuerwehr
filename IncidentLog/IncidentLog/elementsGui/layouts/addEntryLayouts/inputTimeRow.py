from PyQt6.QtCore import QDateTime
from PyQt6.QtWidgets import QHBoxLayout

from elementsGui.buttons.clockButton import ClockButton
from elementsGui.inputWidgets.timeInputWidget import InputTimeWidget
from elementsGui.labels.captionLabel import CaptionLabel


class InputTimeRow(QHBoxLayout):

    def __init__(self, buttonIsVisible: bool = True):
        super().__init__()
        __caption = CaptionLabel("Zeitpunkt")
        self.__clockButton = ClockButton()
        self.__clockButton.setVisible(buttonIsVisible)
        self.__inputTimeWidget = InputTimeWidget()

        self.addWidget(__caption)
        self.addWidget(self.__clockButton)
        self.addWidget(self.__inputTimeWidget)

    def getValue(self) -> str:

        return self.__inputTimeWidget.getCurrentValue()

    def setTimeValue(self, timeString: str):
        self.__inputTimeWidget.setDateTime(QDateTime.fromString(timeString, "dd.MM.yyyy HH:mm"))

    def setDisabled(self):
        self.__inputTimeWidget.setReadOnly(True)
