from PyQt6.QtWidgets import QGroupBox

from elementsGui.layouts.incidentLogLayouts.incidentLogButtonRow import IncidentLogButtonRow


class IncidentLogButtonGroupBox(QGroupBox):

    def __init__(self):
        super().__init__()
        layout = IncidentLogButtonRow()
        self.setLayout(layout)