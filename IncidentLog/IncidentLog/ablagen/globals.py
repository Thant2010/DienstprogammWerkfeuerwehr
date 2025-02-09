import json


file = open("json/global.json", "r", encoding="utf-8")

globalVariables = json.loads(file.read())
file.close()

categorys = globalVariables["categorys"]
reportSender = globalVariables["reportSender"]
iconButtons = globalVariables["iconButtons"]
reportLetter = globalVariables["reportLetter"]
alarmCategory = globalVariables["alarmCategory"]
logTableHeader = globalVariables["logTableHeader"]

colorFile = open("styles/colorTheme.json", "r", encoding="utf-8")
colorTheme = json.loads(colorFile.read())
colorFile.close()
