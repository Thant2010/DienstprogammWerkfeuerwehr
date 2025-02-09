# KI-Generiert - Anpassung fehlt

import json
import os


class Config:
    """
    Diese Klasse lädt die globalen Variablen und das Farbthema aus den
    entsprechenden JSON-Dateien. Dadurch ist der Zugriff zentralisiert
    und die Dateizugriffe erfolgen mittels Context Manager.
    """

    def __init__(self):
        self.__globalData = {}
        self.__colorThemeData = {}

    def load(self):
        self.__loadGlobalVariables()
        self.__loadColorTheme()

    def __loadGlobalVariables(self):
        # Erstelle den absoluten Pfad zur global.json
        base_path = os.path.dirname(__file__)
        global_json_path = os.path.join(base_path, "json", "global.json")
        try:
            with open(global_json_path, "r", encoding="utf-8") as file:
                self.__globalData = json.load(file)
        except Exception as e:
            raise RuntimeError(f"Fehler beim Laden von 'global.json': {e}")

        # Extrahiere die benötigten Schlüssel aus der globalen JSON-Datei
        self.categorys = self.__globalData.get("categorys", [])
        self.reportSender = self.__globalData.get("reportSender", [])
        self.iconButtons = self.__globalData.get("iconButtons", {})
        self.reportLetter = self.__globalData.get("reportLetter", [])
        self.alarmCategory = self.__globalData.get("alarmCategory", [])
        self.logTableHeader = self.__globalData.get("logTableHeader", [])

    def __loadColorTheme(self):
        # Erstelle den absoluten Pfad zur colorTheme.json
        base_path = os.path.dirname(__file__)
        color_json_path = os.path.join(base_path, "styles", "colorTheme.json")
        try:
            with open(color_json_path, "r", encoding="utf-8") as color_file:
                self.__colorThemeData = json.load(color_file)
        except Exception as e:
            raise RuntimeError(f"Fehler beim Laden von 'colorTheme.json': {e}")
        self.colorTheme = self.__colorThemeData


# Erstelle eine Singleton-ähnliche Konfiguration, die beim Import geladen wird.
config = Config()
config.load()

# Exportiere die global verwendeten Variablen
categorys = config.categorys
reportSender = config.reportSender
iconButtons = config.iconButtons
reportLetter = config.reportLetter
alarmCategory = config.alarmCategory
logTableHeader = config.logTableHeader
colorTheme = config.colorTheme
