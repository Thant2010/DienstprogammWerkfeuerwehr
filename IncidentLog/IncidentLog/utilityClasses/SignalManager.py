from PyQt6.QtCore import pyqtSignal, QObject


class SignalManager(QObject):

    onSelectKeyword = pyqtSignal(str, str)
    onEntryIsSaved = pyqtSignal(bool)
    on_set_time_click = pyqtSignal()

    def __init__(self):
        super().__init__()


signalManager = SignalManager()