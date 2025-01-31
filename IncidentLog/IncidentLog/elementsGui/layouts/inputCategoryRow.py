from PyQt6.QtWidgets import QHBoxLayout

from elementsGui.inputWidgets.customInputComboBox import CustomInputComboBox
from elementsGui.labels.captionLabel import CaptionLabel
from utilityFunctions.myMessageBox import MyMessageBox
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