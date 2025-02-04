from PyQt6.QtCore import Qt, pyqtProperty
from PyQt6.QtGui import QColor, QPainter, QPainterPath, QPen
from PyQt6.QtWidgets import QLabel

from utilityClasses.shadowEffect import ShadowEffect


class OutlineTitleLabel(QLabel):

    def __init__(self, caption):
        super().__init__()

        self.setText(caption)
        self.setObjectName("outlineLabel")
        self.setGraphicsEffect(ShadowEffect().shadow)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.__outlineWidth: int = int()
        self.__outlineColor: QColor = QColor()
        self.__textColor: QColor = QColor()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        path = QPainterPath()
        font = self.font()
        text = self.text()

        # Textposition berechnen
        fontMetrics = painter.fontMetrics()
        xPos = 0
        yPos = fontMetrics.ascent()

        path.addText(xPos, yPos, font, text)

        # Umrandung zeichnen
        pen = QPen(self.__outlineColor)
        pen.setWidth(self.__outlineWidth)
        painter.setPen(pen)
        painter.drawPath(path)

        # Text füllen
        painter.fillPath(path, self.__textColor)

    # outlineColor

    def setOutlineColor(self, color):
        if isinstance(color, QColor):
            self.__outlineColor = color
        else:
            self.__outlineColor = QColor(color)
        self.update()

    outlineColor = pyqtProperty(QColor, fset=setOutlineColor)

    # textColor

    def setTextColor(self, color):
        if isinstance(color, QColor):
            self.__textColor = color
        else:
            self.__textColor = QColor(color)
        self.update()

    textColor = pyqtProperty(QColor, fset=setTextColor)

    # outlineWidth
    def setOutlineWidth(self, width):
        if isinstance(width, int):
            self.__outlineWidth = width
        else:
            self.__outlineWidth = 1
        self.update()

    outlineWidth = pyqtProperty(int, fset=setOutlineWidth)
