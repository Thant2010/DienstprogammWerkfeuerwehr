from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QGraphicsDropShadowEffect
from PyQt6.QtGui import QColor


class ShadowEffect:
    """
    Returns a DropShadowEffect
    """
    def __init__(self):
        self.shadow = QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(25)
        self.shadow.setOffset(5, 3)
        self.shadow.setColor(QColor(Qt.GlobalColor.black))
