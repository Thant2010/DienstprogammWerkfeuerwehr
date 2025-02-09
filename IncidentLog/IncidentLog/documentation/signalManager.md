# Signals-Dokumentation

Dieses Dokument listet alle in unserem Projekt verwendeten Signals auf, beschreibt deren Zweck sowie die erwarteten Parameter.

---

## Signal: `on_set_default_values`
- **Sender:** Diverse Widgets (z. B. Input-Felder)
- **Empfänger:** Funktionen, die den Standardzustand wiederherstellen sollen.
- **Parameter:** None
- **Beschreibung:** Wird gesendet, wenn alle Felder in einem Dialog zurückgesetzt werden sollen.

---

## Signal: `on_set_time_click`
- **Sender:** ClockButton
- **Empfänger:** InputTimeWidget
- **Parameter:** None
- **Beschreibung:** Wird gesendet, wenn der Nutzer den Button anklickt, um die aktuelle Zeit zu setzen.

---

## Signal: `on_data_is_valid`
- **Sender:** Eingabefelder (nach Prüfung in einem Formular-Dialog)
- **Empfänger:** Logik zur Verarbeitung bzw. dem Hinzufügen eines neuen Eintrags.
- **Parameter:** (dict) – Ein Dictionary mit folgenden Schlüsseln:
  - `"time"`: (str) Zeitstempel
  - `"category"`: (str) Kategorie des Eintrags
  - `"reportSender"`: (str) Absender des Berichts
  - `"reportText"`: (str) Inhalt des Berichts
- **Beschreibung:** Signalisiert, dass alle Eingabedaten im Formular valide sind und weiterverarbeitet werden können.

---

## Signal: `on_get_row_data`
- **Sender:** IncidentLogTableWidget (benutzerinteraktive Aktion, z. B. Doppelklick)
- **Empfänger:** Fenster, die eine detaillierte Ansicht oder Änderung des Eintrags anzeigen.
- **Parameter:** (dict) – Enthält alle Daten der selektierten Zeile.
- **Beschreibung:** Übermittelt die Daten einer Zeile aus der Tabelle, um diese zu bearbeiten oder anzuzeigen.

---

## Weitere Signale
- `on_save_entry_click` – Signalisiert, dass ein neuer Eintrag gespeichert werden soll.
- `on_change_entry_click` – Signalisiert den Beginn des Änderungsprozesses eines existierenden Eintrags.
- `on_strike_out_row_click` – Signalisiert, dass die aktuelle Tabellenzeile durchgestrichen werden soll.
- `on_new_entry_window_close`, `on_change_entry_window_close`, `on_incident_log_window_close` – Signale zum Schließen der jeweiligen Fenster.
- `on_insert_changes` – Signalisiert, dass geänderte Daten in einen bestehenden Eintrag übernommen werden sollen.
- `on_get_change` – Übermittelt einen Nachtrag (z. B. in Form eines Strings und Zeitstempels) zur Aktualisierung eines Eintrags.

---

Dieses Dokument sollte bei jeder Erweiterung um neue Signals aktualisiert werden, sodass alle Entwickler stets den Überblick über die interne Kommunikation per Signals haben.
