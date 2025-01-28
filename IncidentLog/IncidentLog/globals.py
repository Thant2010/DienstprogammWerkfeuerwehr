import json


file = open("json/global.json", "r", encoding="utf-8")

globalVariables = json.loads(file.read())

categorys = globalVariables["categorys"]