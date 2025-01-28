from PyQt6.QtWidgets import QHBoxLayout

from elementsGui.inputWidgets.categoryComboBox import CategoryComboBox
from elementsGui.labels.captionLabel import CaptionLabel


class InputCategoryRow(QHBoxLayout):

    def __init__(self):
        super().__init__()
        caption = CaptionLabel("Kategorie")
        self.__categoryComboBox = CategoryComboBox()

        self.addWidget(caption)
        self.addWidget(self.__categoryComboBox)