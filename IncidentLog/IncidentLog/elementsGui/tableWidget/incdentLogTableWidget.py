from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QTableWidget, QFrame, QHeaderView, QSizePolicy

from elementsGui.tableWidget.customTableRow import CustomTableRow
from globals import logTableHeader
from utilityClasses.signalManager import signalManager


class IncidentLogTableWidget(QTableWidget):
    maxHeigt = 500

    def __init__(self):
        super().__init__()
        signalManager.on_data_is_valid.connect(self.__addNewEntryRow)

        self.__currentSortOrder = Qt.SortOrder.AscendingOrder

        self.setProperty("fontsize", "small")
        self.setCornerButtonEnabled(False)
        self.setFrameShape(QFrame.Shape.Box)
        self.setFrameShadow(QFrame.Shadow.Sunken)
        self.setWordWrap(True)
        self.setColumnCount(len(logTableHeader))
        self.setHorizontalHeaderLabels(logTableHeader)
        self.setSizePolicy(QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred))

        self.verticalHeader().setVisible(False)
        self.horizontalHeader().sectionDoubleClicked.connect(self.__onHeaderClicked)

        self.__setColumnWidth()
        self.__updateHeight()

    def __sortTable(self, columnToSort):
        self.sortItems(columnToSort, self.__currentSortOrder)

    def __onHeaderClicked(self, columnToSort):

        if self.__currentSortOrder == Qt.SortOrder.AscendingOrder:
            self.__currentSortOrder = Qt.SortOrder.DescendingOrder
            self.__sortTable(columnToSort)
        else:
            self.__currentSortOrder = Qt.SortOrder.AscendingOrder
            self.__sortTable(columnToSort)

    def __setColumnWidth(self):
        self.setColumnWidth(0, 60)
        self.setColumnWidth(1, 140)
        self.setColumnWidth(2, 110)
        self.setColumnWidth(3, 125)

        self.horizontalHeader().setSectionResizeMode(4, QHeaderView.ResizeMode.Stretch)

    def __addNewEntryRow(self, newEntryDict: dict):
        self.insertRow(self.rowCount())
        newEntryRow = CustomTableRow(self.rowCount(), newEntryDict)
        newEntryRow.getRowItems(self)
        self.resizeRowsToContents()
        self.__updateHeight()

    def __updateHeight(self):
        totalRowHeight = sum(self.rowHeight(row) for row in range(self.rowCount()))
        totalHeight = self.horizontalHeader().height() + totalRowHeight + 2
        newHeight = min(totalHeight, self.maxHeigt)
        self.setMinimumHeight(newHeight)