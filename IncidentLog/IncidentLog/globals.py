import json
from pathlib import Path


class Config:
    """
    Lädt Konfigurationsdaten (globale Variablen und Farbthema) aus JSON-Dateien.
    """

    def __init__(self):
        self._global_data = {}
        self._color_theme_data = {}

    def load(self) -> None:
        self._load_global_variables()
        self._load_color_theme()

    def _load_json_file(self, path: Path) -> dict:
        try:
            with path.open("r", encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            raise RuntimeError(f"Datei nicht gefunden: {path}")
        except json.JSONDecodeError as e:
            raise RuntimeError(f"Fehler beim Parsen der Datei '{path}': {e}")
        except Exception as e:
            raise RuntimeError(f"Fehler beim Laden der Datei '{path}': {e}")

    def _load_global_variables(self) -> None:
        base_path = Path(__file__).parent
        global_json_path = base_path / "json" / "global.json"
        self._global_data = self._load_json_file(global_json_path)

        # Benutze 'categories' statt 'categorys', falls möglich.
        self.categories = self._global_data.get("categories", [])
        self.reportSender = self._global_data.get("reportSender", [])
        self.iconButtons = self._global_data.get("iconButtons", {})
        self.reportLetter = self._global_data.get("reportLetter", [])
        self.alarmCategory = self._global_data.get("alarmCategory", [])
        self.logTableHeader = self._global_data.get("logTableHeader", [])
        self.unitsTableHeader = self._global_data.get("unitsTableHeader", [])
        self.incidentLogPath = self._global_data.get("incidentLogPath", base_path)
        self.externalUnits = self._global_data.get("externalUnits", [])

    def _load_color_theme(self) -> None:
        base_path = Path(__file__).parent
        color_json_path = base_path / "styles" / "colorTheme.json"
        self._color_theme_data = self._load_json_file(color_json_path)
        self.colorTheme = self._color_theme_data

# Erstelle eine Singleton-ähnliche Konfiguration, die beim Import geladen wird.
config = Config()
config.load()

# Exportiere die global verwendeten Variablen
categorys = config.categories
reportSender = config.reportSender
iconButtons = config.iconButtons
reportLetter = config.reportLetter
alarmCategory = config.alarmCategory
logTableHeader = config.logTableHeader
colorTheme = config.colorTheme
incidentLogPath = config.incidentLogPath
unitsTableHeader = config.unitsTableHeader
externalUnits = config.externalUnits