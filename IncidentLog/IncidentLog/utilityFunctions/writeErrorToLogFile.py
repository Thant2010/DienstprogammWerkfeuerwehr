import getpass
from datetime import datetime


def writeErrorToLogFile(error: str) -> None:
    """
    Write an Error/Exception to a LogFile
    :param error: Error as String
    """

    logFile = open("log.txt", "a")
    logFile.write(f"--> {datetime.now().strftime('%d.%m.%Y %H:%M')}"
                  f"\n--> Benutzer: {getpass.getuser()}\n--> {error}\n\n")
    logFile.close()

