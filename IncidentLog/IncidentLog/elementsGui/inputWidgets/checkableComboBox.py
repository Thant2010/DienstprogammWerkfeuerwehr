from PyQt6.QtCore import Qt
from PyQt6.QtGui import QStandardItem, QStandardItemModel
from PyQt6.QtWidgets import QComboBox

from utilityClasses.signalManager import signalManager


class CheckableComboBox(QComboBox):

    def __init__(self, comboList: list):
        super().__init__()

        signalManager.on_set_default_values.connect(self.__uncheckAll)

        self.setMinimumSize(200, 30)
        self.setProperty("selectable", True)

        self.setEditable(True)
        self.lineEdit().setReadOnly(True)
        self.lineEdit().setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.setInsertPolicy(QComboBox.InsertPolicy.NoInsert)
        self.setModel(QStandardItemModel(self))

        for entry in comboList:
            self.addItem(entry)
        self.setMaxVisibleItems(self.count())
        self.__updateText()
        self.view().pressed.connect(self.__handleItemPressed)

    def getCheckedText(self):
        return self.__getCheckedItems()

    def addItem(self, text, data=None):
        item = QStandardItem(text)
        item.setFlags(Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsUserCheckable)
        item.setData(data)
        item.setCheckState(Qt.CheckState.Unchecked)
        self.model().appendRow(item)

    def __handleItemPressed(self, index):
        item = self.model().itemFromIndex(index)
        if item.checkState() == Qt.CheckState.Checked:
            item.setCheckState(Qt.CheckState.Unchecked)
        else:
            item.setCheckState(Qt.CheckState.Checked)
        self.__updateText()

    def __uncheckAll(self):
        for index in range(self.model().rowCount()):
            item = self.model().item(index)
            item.setCheckState(Qt.CheckState.Unchecked)
        self.__updateText()

    def __getCheckedItems(self):
        items = []
        for index in range(self.model().rowCount()):
            item = self.model().item(index)
            if item.checkState() == Qt.CheckState.Checked:
                items.append(item.text())
        return items

    def __updateText(self):
        checkedItems = self.getCheckedText()
        num_selected = len(checkedItems)
        self.lineEdit().setText(f"Ausgewählt ({num_selected})")