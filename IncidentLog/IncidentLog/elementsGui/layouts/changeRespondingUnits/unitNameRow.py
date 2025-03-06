from PyQt6.QtWidgets import QHBoxLayout

from elementsGui.inputWidgets.customLineEdit import CustomLineEdit
from elementsGui.labels.captionLabel import CaptionLabel


class UnitNameRow(QHBoxLayout):

    def __init__(self):
        super().__init__()
        caption = CaptionLabel("Einheit")
        self.__unitName = CustomLineEdit()
        self.__unitName.setEnabled(False)

        self.addWidget(caption)
        self.addWidget(self.__unitName)

    def setUnitName(self, unitName: str):
        self.__unitName.setText(unitName)

    def getUnitName(self) -> str:
        return self.__unitName.getValue()