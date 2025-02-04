from PyQt6.QtWidgets import QHBoxLayout

from elementsGui.inputWidgets.customLineEdit import CustomLineEdit
from elementsGui.labels.captionLabel import CaptionLabel


class InputAlarmAreaRow(QHBoxLayout):

    def __init__(self):
        super().__init__()
        caption = CaptionLabel("Halle / Bereich")
        self.__inputAlarmArea = CustomLineEdit()


        self.addWidget(caption)
        self.addWidget(self.__inputAlarmArea)
