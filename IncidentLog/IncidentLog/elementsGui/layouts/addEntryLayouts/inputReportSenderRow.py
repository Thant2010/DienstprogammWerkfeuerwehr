from PyQt6.QtWidgets import QHBoxLayout

from elementsGui.inputWidgets.customInputComboBox import CustomInputComboBox
from elementsGui.labels.captionLabel import CaptionLabel
from globals import reportSender


class InputReportSenderRow(QHBoxLayout):

    def __init__(self):
        super().__init__()

        caption = CaptionLabel("Absender")
        self.__reportSenderComboBox = CustomInputComboBox(comboList=reportSender, readOnly=False)
        self.__reportSenderComboBox.setToolTip("Eintrag wählen oder Editiern")

        self.addWidget(caption)
        self.addWidget(self.__reportSenderComboBox)

    def getValue(self) -> str:
        return self.__reportSenderComboBox.currentText()

    def setDisabled(self):
        self.__reportSenderComboBox.setDisabled(True)

    def setReportSender(self, sender):
        index = self.__reportSenderComboBox.findText(sender)
        self.__reportSenderComboBox.setCurrentIndex(index)