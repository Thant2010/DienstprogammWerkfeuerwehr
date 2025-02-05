from PyQt6.QtCore import pyqtSignal, QObject


class SignalManager(QObject):

    on_set_default_values = pyqtSignal()
    on_set_time_click = pyqtSignal()

    on_data_is_valid = pyqtSignal(dict)
    on_get_row_data = pyqtSignal(dict)
    on_save_entry_click = pyqtSignal()
    on_save_changes_click = pyqtSignal()
    on_add_new_entry_click = pyqtSignal()
    on_change_entry_click = pyqtSignal()

    on_get_change = pyqtSignal(str, str, str)
    on_insert_changes = pyqtSignal(dict)

    # Close Signale
    on_new_entry_window_close = pyqtSignal()
    on_change_entry_window_close = pyqtSignal()
    on_incident_log_window_close = pyqtSignal()

    def __init__(self):
        super().__init__()


signalManager = SignalManager()