from PyQt6.QtCore import pyqtSignal, QObject


class SignalManager(QObject):
    """
      Der zentrale Signal-Manager.

      Signals:
          on_set_default_values:        Signal für das Zurücksetzen auf Standardwerte (keine Parameter).
          on_log_data_is_valid:             Signal, das ein dict (Log Eintragsdaten) sendet, wenn Daten validiert wurden.
          on_unit_data_is_valid:        Signal, das ein dict (Einheiten) sendet, wenn Daten validiert wurden.
          on_get_row_data:              Signal, das ein dict mit Zeilendaten überträgt.
          on_save_entry_click:          Signal, wenn ein neuer Eintrag gespeichert werden soll.
          on_add_unit_click:            Signal, wenn Einsatzkräfte hinzugefügt werden sollen.
          on_save_changes_click:        Signal, wenn Änderungen gespeichert werden sollen.
          on_add_new_entry_click:       Signal, wenn ein neuer Eintrag begonnen wird.
          on_change_entry_click:        Signal, wenn ein existierender Eintrag geändert werden soll.
          on_strike_out_row_click:      Signal, um eine Zeile in der Tabelle durchzustreichen.
          on_get_change:                Signal, das zwei Strings (z.B. Änderungsnachricht und Zeitstempel) sendet.
          on_insert_changes:            Signal, das ein dict mit geänderten Daten überträgt.
          on_new_entry_window_close:    Signal zum Schließen des Fensters für neue Einträge.
          on_change_entry_window_close: Signal zum Schließen des Änderungsfensters.
          on_incident_log_window_close: Signal zum Schließen des Hauptfensters.
      """

    on_set_default_values = pyqtSignal()

    on_log_data_is_valid = pyqtSignal(dict)
    on_unit_data_is_valid = pyqtSignal(dict)
    on_get_row_data = pyqtSignal(dict)
    on_save_entry_click = pyqtSignal()
    on_save_changes_click = pyqtSignal()
    on_add_new_entry_click = pyqtSignal()
    on_add_unit_click = pyqtSignal()
    on_change_entry_click = pyqtSignal()
    on_strike_out_row_click = pyqtSignal()

    on_get_change = pyqtSignal(str, str)
    on_insert_changes = pyqtSignal(dict)

    on_new_entry_window_close = pyqtSignal()
    on_change_entry_window_close = pyqtSignal()
    on_incident_log_window_close = pyqtSignal()

    def __init__(self):
        super().__init__()


signalManager = SignalManager()