from PyQt6.QtWidgets import QSpacerItem, QSizePolicy


class LayoutSpacer:

    @staticmethod
    def verticalExpandingSpacer():
        spacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        return spacer

    @staticmethod
    def horizontalExpandingSpacer():
        spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        return spacer

    @staticmethod
    def verticalFixedSpacer(height):
        spacer = QSpacerItem(20, height, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        return spacer

    @staticmethod
    def horizontalFixedSpacer(width):
        spacer = QSpacerItem(width, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)
        return spacer

