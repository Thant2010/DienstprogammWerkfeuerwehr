from PyQt6.QtWidgets import QHBoxLayout

from elementsGui.inputWidgets.customInputComboBox import CustomInputComboBox
from elementsGui.labels.captionLabel import CaptionLabel
from globals import categorys


class InputCategoryRow(QHBoxLayout):

    def __init__(self):
        super().__init__()
        caption = CaptionLabel("Kategorie")
        self.__categoryComboBox = CustomInputComboBox("Kategorie", categorys, True)

        self.addWidget(caption)
        self.addWidget(self.__categoryComboBox)

    def getValue(self) -> str:
        return self.__categoryComboBox.currentText()

    def setDisabled(self):
        self.__categoryComboBox.setDisabled(True)

    def setCategoryValue(self, category):
        index = self.__categoryComboBox.findText(category)
        self.__categoryComboBox.setCurrentIndex(index)