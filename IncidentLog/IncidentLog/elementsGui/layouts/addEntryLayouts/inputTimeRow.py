from PyQt6.QtCore import QDateTime
from PyQt6.QtWidgets import QHBoxLayout

from elementsGui.buttons.clockButton import ClockButton
from elementsGui.inputWidgets.timeInputWidget import InputTimeWidget
from elementsGui.labels.captionLabel import CaptionLabel


class InputTimeRow(QHBoxLayout):

    def __init__(self, caption,  buttonIsVisible: bool = True, clearTimeWidget: bool = False):
        super().__init__()
        __caption = CaptionLabel(caption)
        self.__clockButton = ClockButton()
        self.__clockButton.setVisible(buttonIsVisible)
        self.__clockButton.clicked.connect(self.__setCurrentTime)
        self.__inputTimeWidget = InputTimeWidget(clearTimeWidget)

        self.addWidget(__caption)
        self.addWidget(self.__clockButton)
        self.addWidget(self.__inputTimeWidget)

    def getValue(self) -> str:

        return self.__inputTimeWidget.getCurrentValue()

    def setTimeValue(self, timeString: str):
        if timeString != "":
            self.__inputTimeWidget.setDisabled(False)
            self.__inputTimeWidget.setDateTime(QDateTime.fromString(timeString, "dd.MM.yyyy HH:mm"))


    def setDisabled(self):
        self.__inputTimeWidget.setReadOnly(True)

    def __setCurrentTime(self):
        self.__inputTimeWidget.setCurrentDateTime()