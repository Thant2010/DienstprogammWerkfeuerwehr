from PyQt6.QtWidgets import QHBoxLayout

from elementsGui.inputWidgets.customLineEdit import CustomLineEdit
from elementsGui.labels.captionLabel import CaptionLabel


class InputChangesRow(QHBoxLayout):

    def __init__(self):
        super().__init__()
        caption = CaptionLabel("Nachtrag")
        self.__inputChanges = CustomLineEdit()

        self.addWidget(caption)
        self.addWidget(self.__inputChanges)

    def getInputValue(self):
        if self.__inputChanges.text() != "":
            return self.__inputChanges.text()
        else:
            return None