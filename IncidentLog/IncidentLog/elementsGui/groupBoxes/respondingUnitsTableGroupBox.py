from PyQt6.QtWidgets import QGroupBox, QGridLayout

from elementsGui.tableWidget.respondingUnitsTableWidget import RespondingUnitsTableWidget


class RespondingUnitsGroupBox(QGroupBox):

    def __init__(self):
        super().__init__()
        layout = QGridLayout()

        self.__respondingUnitsTable = RespondingUnitsTableWidget()

        layout.addWidget(self.__respondingUnitsTable, 0, 0)

        self.setLayout(layout)