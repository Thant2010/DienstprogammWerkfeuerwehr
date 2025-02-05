from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QHBoxLayout

from elementsGui.inputWidgets.inputReportTextWidget import InputReportTextWidget
from elementsGui.labels.captionLabel import CaptionLabel

class InputReportTextRow(QHBoxLayout):
    def __init__(self):
        super().__init__()
        caption = CaptionLabel("Text")
        self.__inputReportText = InputReportTextWidget()

        self.addWidget(caption, alignment=Qt.AlignmentFlag.AlignTop)
        self.addWidget(self.__inputReportText)

    def getValue(self) -> str:
        return self.__inputReportText.getInput()

    def setDiabled(self):
        self.__inputReportText.setReadOnly(True)

    def setReportText(self, text):
        self.__inputReportText.setPlainText(text)