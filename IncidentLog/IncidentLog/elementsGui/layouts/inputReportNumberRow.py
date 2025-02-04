from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIntValidator
from PyQt6.QtWidgets import QHBoxLayout

from elementsGui.inputWidgets.customInputComboBox import CustomInputComboBox
from elementsGui.inputWidgets.customLineEdit import CustomLineEdit
from elementsGui.labels.captionLabel import CaptionLabel
from globals import reportLetter
from utilityClasses.layoutSpacer import LayoutSpacer


class InputReportNumberRow(QHBoxLayout):

    def __init__(self):
        super().__init__()
        caption = CaptionLabel("Bericht")
        caption.setFixedWidth(150)
        self.__comboReportLetter = CustomInputComboBox("Bericht", reportLetter, True)
        self.__comboReportLetter.setFixedSize(80, 30)
        self.__inputReportNumber = CustomLineEdit()
        self.__inputReportNumber.setFixedSize(60, 30)
        self.__inputReportNumber.setValidator(QIntValidator(000, 999))
        self.__inputReportNumber.setMaxLength(3)
        self.__inputReportNumber.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.addWidget(caption)
        self.addWidget(self.__comboReportLetter)
        self.addWidget(self.__inputReportNumber)
        self.addItem(LayoutSpacer.horizontalExpandingSpacer())