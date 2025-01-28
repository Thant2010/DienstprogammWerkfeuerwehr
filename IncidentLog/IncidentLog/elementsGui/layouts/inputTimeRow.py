from PyQt6.QtWidgets import QHBoxLayout

from elementsGui.buttons.clockButton import ClockButton
from elementsGui.inputWidgets.timeInputWidget import InputTimeWidget
from elementsGui.labels.captionLabel import CaptionLabel


class InputTimeRow(QHBoxLayout):

    def __init__(self):
        super().__init__()
        __caption = CaptionLabel("Zeitpunkt")
        self.__inputTimeWidget = InputTimeWidget()
        self.__clockButton = ClockButton()

        self.addWidget(__caption)
        self.addWidget(self.__clockButton)
        self.addWidget(self.__inputTimeWidget)


    def getValue(self):
        print(self.__inputTimeWidget.getCurrentValue())
        print(self.__inputTimeWidget.getCurrenTime())
        print(self.__inputTimeWidget.getCurrenDate())