from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QHBoxLayout

from elementsGui.inputWidgets.customInputComboBox import CustomInputComboBox
from elementsGui.labels.captionLabel import CaptionLabel
from globals import alarmCategory
from utilityClasses.layoutSpacer import LayoutSpacer


class InputAlarmCategoryRow(QHBoxLayout):

    def __init__(self):
        super().__init__()
        caption = CaptionLabel("Einsatzart")

        self.__comboAlarmCategory = CustomInputComboBox("Einsatzart", alarmCategory, True)
        self.__comboAlarmCategory.setMinimumWidth(280)

        self.addWidget(caption)
        self.addWidget(self.__comboAlarmCategory)
        self.addItem(LayoutSpacer.horizontalExpandingSpacer())
