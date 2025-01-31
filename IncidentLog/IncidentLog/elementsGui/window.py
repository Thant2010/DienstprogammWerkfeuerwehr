from PyQt6.QtWidgets import QWidget, QGridLayout

from elementsGui.layouts.buttonLayoutRow import ButtonLayoutRow
from elementsGui.layouts.inputCategoryRow import InputCategoryRow
from elementsGui.layouts.inputReportSenderRow import InputReportSender
from elementsGui.layouts.inputReportTextRow import InputReportText
from elementsGui.layouts.inputTimeRow import InputTimeRow
from utilityClasses.SignalManager import signalManager
from utilityClasses.LayoutSpacer import LayoutSpacer
class Window(QWidget):

    def __init__(self):
        super().__init__()

        signalManager.on_save_entry_click.connect(self.__saveValues)
        signalManager.on_entry_window_close.connect(self.close)

        __layout = QGridLayout()
        self.timeEdit = InputTimeRow()
        self.category = InputCategoryRow()
        self.reportSender = InputReportSender()
        self.reportText = InputReportText()
        self.buttonRow = ButtonLayoutRow()

        __layout.addLayout(self.timeEdit, 0, 0)
        __layout.addLayout(self.category, 1, 0)
        __layout.addLayout(self.reportSender, 2, 0)
        __layout.addLayout(self.reportText, 0, 1, 3, 1)
        __layout.addItem(LayoutSpacer.verticalFixedSpacer(25))
        __layout.addLayout(self.buttonRow, 4, 0, 1, -1)

        self.setLayout(__layout)
        self.show()

    def __saveValues(self):
        time = self.timeEdit.getValue()
        category = self.category.getValue()
        reportSender = self.reportSender.getValue()
        reportText = self.reportText.getValue()
        newEntry = {
            "time": time,
            "category": category,
            "reportSender": reportSender,
            "reportText": reportText
        }

        for value in newEntry.values():
            if value is None:
                return

        signalManager.on_set_default_values()
        signalManager.on_successful_save.emit(newEntry)

        print(newEntry)


