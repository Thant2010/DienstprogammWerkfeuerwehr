from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QTableWidget, QFrame, QSizePolicy, QAbstractItemView


class CustomTableWidget(QTableWidget):
    MAX_HEIGHT = 400

    def __init__(self, headerList: list):
        super().__init__()

        self.__currentSortOrder = Qt.SortOrder.AscendingOrder

        self.setProperty("fontsize", "small")
        self.setCornerButtonEnabled(False)
        self.setFrameShape(QFrame.Shape.Box)
        self.setFrameShadow(QFrame.Shadow.Sunken)
        self.setWordWrap(True)

        self.setColumnCount(len(headerList))
        self.setHorizontalHeaderLabels(headerList)

        self.setSizePolicy(QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred))
        self.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)

        self.verticalHeader().setVisible(False)
        self.horizontalHeader().sectionDoubleClicked.connect(self.__onHeaderClicked)

    def __sortTable(self, columnToSort):
        self.sortItems(columnToSort, self.__currentSortOrder)

    def __onHeaderClicked(self, columnToSort):

        if self.__currentSortOrder == Qt.SortOrder.AscendingOrder:
            self.__currentSortOrder = Qt.SortOrder.DescendingOrder
            self.__sortTable(columnToSort)
        else:
            self.__currentSortOrder = Qt.SortOrder.AscendingOrder
            self.__sortTable(columnToSort)

