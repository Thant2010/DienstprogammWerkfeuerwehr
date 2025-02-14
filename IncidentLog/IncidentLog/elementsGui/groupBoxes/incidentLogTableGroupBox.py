from PyQt6.QtWidgets import QGroupBox, QGridLayout

from elementsGui.tableWidget.incdentLogTableWidget import IncidentLogTableWidget


class IncidentLogTableGroupBox(QGroupBox):

    def __init__(self):
        super().__init__()
        layout = QGridLayout()

        self.__incidentLogTable = IncidentLogTableWidget()

        layout.addWidget(self.__incidentLogTable, 0, 0)

        self.setLayout(layout)