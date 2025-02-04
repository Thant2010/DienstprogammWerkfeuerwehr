from PyQt6.QtCore import pyqtSignal, QObject


class SignalManager(QObject):

    on_set_default_values = pyqtSignal()
    on_set_time_click = pyqtSignal()
    on_entry_window_close = pyqtSignal()
    on_save_entry_click = pyqtSignal()
    on_data_is_valid = pyqtSignal(dict)
    on_add_new_entry = pyqtSignal()

    def __init__(self):
        super().__init__()


signalManager = SignalManager()