import win32api
from PyQt6.QtCore import QDateTime


class GetTimeStamp:

    @staticmethod
    def getTimeStamp():
        dateTime = QDateTime.currentDateTime().toString("dd.MM.yyyy HH:mm")
        user = GetTimeStamp.__getFullUserName()

        return f'{user}, {dateTime}'

    @staticmethod
    def __getFullUserName():
        try:
            # Gibt den vollständigen Namen des Benutzers zurück
            return win32api.GetUserNameEx(3)  # 3 steht für "FullName"
        except Exception as e:
            print(f"Fehler: {e}")
            return None