from PyQt6.QtCore import QDateTime


def getCurrentDateTime() -> str:
    return QDateTime.currentDateTime().toString("dd.MM.yyyy HH:mm")