from PyQt6.QtWidgets import QTableWidget

from elementsGui.tableWidget.customTableWidgetItem import CustomTableWidgetItem


class RespondingUnitRow:

    def __init__(self, unitValues: dict):
        self.__rowItems = list()
        self.__createRowItems(unitValues)

    def __createRowItems(self, newEntryDict: dict):
        for key in newEntryDict.keys():
            self.__rowItems.append(CustomTableWidgetItem(newEntryDict[key], key))

    def getRowItems(self, tableWidget: QTableWidget):
        row = tableWidget.rowCount() - 1
        for i, item in enumerate(self.__rowItems):
            tableWidget.setItem(row, i, item)
