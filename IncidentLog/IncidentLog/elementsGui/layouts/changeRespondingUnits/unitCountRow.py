from PyQt6.QtWidgets import QHBoxLayout

from elementsGui.inputWidgets.customIntegerLineEdit import CustomIntegerLineEdit
from elementsGui.labels.captionLabel import CaptionLabel
from utilityClasses.layoutSpacer import LayoutSpacer


class UnitCountsRow(QHBoxLayout):

    def __init__(self):
        super().__init__()

        caption = CaptionLabel("Anzahl:")
        self.__unitsCount = CustomIntegerLineEdit()

        self.addWidget(caption)
        self.addWidget(self.__unitsCount)
        self.addItem(LayoutSpacer.horizontalExpandingSpacer())

    def setUnitsCount(self, count: int):
        self.__unitsCount.setText(str(count))

    def getUnitsCount(self) -> str:
        if self.__unitsCount.text() != "0":
            unitCount = self.__unitsCount.text()
        else:
            unitCount = "-"

        return unitCount