import win32api


def getFullUserName():
    try:
        # Gibt den vollständigen Namen des Benutzers zurück
        return win32api.GetUserNameEx(3)  # 3 steht für "FullName"
    except Exception as e:
        print(f"Fehler: {e}")
        return None