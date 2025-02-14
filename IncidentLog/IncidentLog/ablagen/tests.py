import sys
import time
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import QApplication, QComboBox, QLineEdit, QVBoxLayout, QWidget, QPushButton


class CheckableComboBox(QComboBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        # Die Combobox soll "editable" sein, damit wir den Text zur Anzeige der Auswahl nutzen können,
        # aber der Benutzer soll nicht direkt in das Feld schreiben können.
        self.setEditable(True)
        self.lineEdit().setReadOnly(True)
        self.lineEdit().setPlaceholderText('Einheiten auswählen')
        # Preventing QComboBox from trying to insert new items automatically.
        self.setInsertPolicy(QComboBox.InsertPolicy.NoInsert)
        self.setModel(QStandardItemModel(self))
        # Verbindung des Klicks in der Ansicht auf die Methode, die das Häkchen umschaltet.
        self.view().pressed.connect(self.handle_item_pressed)

    def handle_item_pressed(self, index):
        """Schaltet den Checkzustand des angeklickten Elements um und aktualisiert den angezeigten Text."""
        item = self.model().itemFromIndex(index)
        if item.checkState() == Qt.CheckState.Checked:
            item.setCheckState(Qt.CheckState.Unchecked)
        else:
            item.setCheckState(Qt.CheckState.Checked)
        self.updateText()

    def updateText(self):
        """Aktualisiert den Text im LineEdit der Combobox anhand der ausgewählten Elemente."""
        checkedItems = []
        for index in range(self.model().rowCount()):
            item = self.model().item(index)
            if item.checkState() == Qt.CheckState.Checked:
                checkedItems.append(item.text())
        self.lineEdit().setText(', '.join(checkedItems))

    def addItem(self, text, data=None):
        """Fügt einen Eintrag als checkable Item hinzu."""
        item = QStandardItem(text)
        item.setFlags(Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsUserCheckable)
        # Möglichkeit, zusätzliche Daten zu speichern
        item.setData(data)
        item.setCheckState(Qt.CheckState.Unchecked)
        self.model().appendRow(item)

    def addItems(self, texts):
        """Fügt eine Liste von Einträgen hinzu."""
        for text in texts:
            self.addItem(text)

    def checkedItems(self):
        """Gibt eine Liste der aktuell ausgewählten Elemente zurück."""
        items = []
        for index in range(self.model().rowCount()):
            item = self.model().item(index)
            if item.checkState() == Qt.CheckState.Checked:
                items.append(item.text())
        return items


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Hauptfenster und Layout
    window = QWidget()
    layout = QVBoxLayout(window)

    # Instanz der CheckableComboBox
    combo = CheckableComboBox()

    # Grundlegende Einträge aus einer Liste
    einheiten = ["m", "km", "cm", "mm", "in", "ft"]
    combo.addItems(einheiten)
    layout.addWidget(combo)


    # Button, um die aktuelle Auswahl zusammen mit einem Zeitstempel zu verarbeiten
    def process_selection():
        ausgewählte_einträge = combo.checkedItems()
        current_time = time.time()
        print(f"Ausgewählte Einträge ({current_time}): {ausgewählte_einträge}")


    prozess_button = QPushButton("Auswahl verarbeiten")
    prozess_button.clicked.connect(process_selection)
    layout.addWidget(prozess_button)

    # Eingabefeld und Button zum manuellen Hinzufügen von Einträgen
    manual_entry = QLineEdit()
    manual_entry.setPlaceholderText("Neue Einheit eingeben")
    layout.addWidget(manual_entry)


    def add_manual():
        text = manual_entry.text().strip()
        if text:
            combo.addItem(text)
            manual_entry.clear()


    add_manual_button = QPushButton("Manuell hinzufügen")
    add_manual_button.clicked.connect(add_manual)
    layout.addWidget(add_manual_button)

    window.setWindowTitle("Mehrfachauswahl mit CheckableComboBox")
    window.show()
    sys.exit(app.exec())
