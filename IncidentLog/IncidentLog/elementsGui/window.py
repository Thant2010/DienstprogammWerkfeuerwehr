from PyQt6.QtCore import QTime
from PyQt6.QtWidgets import QWidget, QGridLayout

from elementsGui.buttons.clockButton import ClockButton
from elementsGui.inputWidgets.categoryComboBox import CategoryComboBox
from elementsGui.inputWidgets.timeInputWidget import InputTimeWidget
from elementsGui.layouts.inputCategoryRow import InputCategoryRow
from elementsGui.layouts.inputTimeRow import InputTimeRow
from utilityClasses.SignalManager import signalManager
class Window(QWidget):

    def __init__(self):
        super().__init__()

        __layout = QGridLayout()
        self.timeEdit = InputTimeRow()
        self.category = InputCategoryRow()
        combo = CategoryComboBox()

        __layout.addLayout(self.timeEdit, 0, 0)
        __layout.addLayout(self.category, 1, 0)

        self.setLayout(__layout)
        self.show()



