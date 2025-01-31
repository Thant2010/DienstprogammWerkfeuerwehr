from PyQt6.QtCore import pyqtSignal, QObject


class SignalManager(QObject):

    on_set_default_values = pyqtSignal()
    on_set_time_click = pyqtSignal()
    on_entry_window_close = pyqtSignal()
    on_save_entry_click = pyqtSignal()
    on_successful_save = pyqtSignal(dict)

    def __init__(self):
        super().__init__()


signalManager = SignalManager()