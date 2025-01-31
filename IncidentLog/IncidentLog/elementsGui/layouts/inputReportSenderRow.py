from PyQt6.QtWidgets import QHBoxLayout

from elementsGui.inputWidgets.customInputComboBox import CustomInputComboBox
from elementsGui.labels.captionLabel import CaptionLabel
from globals import reportSender
from utilityFunctions.myMessageBox import MyMessageBox


class InputReportSender(QHBoxLayout):

    def __init__(self):
        super().__init__()
        caption = CaptionLabel("Absender")
        self.__reportSenderComboBox = CustomInputComboBox("Absender", reportSender, False)
        self.__reportSenderComboBox.setToolTip("Eintrag wählen oder Editiern")
        self.addWidget(caption)
        self.addWidget(self.__reportSenderComboBox)

    def getValue(self) -> str:
        return self.__reportSenderComboBox.currentText()