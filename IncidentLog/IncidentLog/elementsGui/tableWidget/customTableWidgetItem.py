from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QTableWidgetItem


class CustomTableWidgetItem(QTableWidgetItem):

    def __init__(self, value: str, dictKey: str, alignment: str = "center"):
        super().__init__()
        self.setText(value)
        self.setFlags((Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled))
        self.__dictKey = dictKey
        self.__setAlignmentFlag(alignment)

    def __setAlignmentFlag(self, alignment: str):
        match alignment:
            case "center":
                self.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                return
            case "left":
                self.setTextAlignment(Qt.AlignmentFlag.AlignLeft)
                return
            case "right":
                self.setTextAlignment(Qt.AlignmentFlag.AlignRight)
                return

    def getItemValue(self) -> dict:
        return self.__dictKey, self.text()

    def setValue(self, value: str):
        self.setText(value)

