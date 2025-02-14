from utilityClasses.getTimeStamp import GetTimeStamp


def writeErrorToLogFile(error: str) -> None:
    """
    Write an Error/Exception to a LogFile
    :param error: Error as String
    """

    logFile = open("log.txt", "a")
    logFile.write(f"--> {GetTimeStamp.getTimeStamp()}"
                  f"\n--> {error}\n\n")
    logFile.close()

