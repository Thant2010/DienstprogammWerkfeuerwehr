from PyQt6.QtWidgets import QHBoxLayout

from elementsGui.inputWidgets.customLineEdit import CustomLineEdit
from elementsGui.labels.captionLabel import CaptionLabel


class InputAlarmEventRow(QHBoxLayout):

    def __init__(self):
        super().__init__()
        caption = CaptionLabel("Schadensereignis")
        self.__inputAlarmEvent = CustomLineEdit()

        self.addWidget(caption)
        self.addWidget(self.__inputAlarmEvent)
