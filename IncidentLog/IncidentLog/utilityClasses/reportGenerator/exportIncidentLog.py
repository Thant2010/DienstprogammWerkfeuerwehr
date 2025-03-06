from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Paragraph
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Spacer, PageBreak

from globals import incidentLogPath
from utilityClasses.reportGenerator.strikeTroughParagraph import StrikeThroughParagraph


class IncidentLogReportGenerator:

    def __init__(self):
        self.__document = SimpleDocTemplate(filename="", pagesize=A4)
        self.__styles = getSampleStyleSheet()
        self.__reportStory = []
        self.__cellStyle = ParagraphStyle(name="CellStyle",
                                          parent=self.__styles["BodyText"],
                                          alignment=0,  # linksbündig
                                          leading=12,
                                          spaceAfter=4)
        self.__tableStyle = [("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
                            ("TEXTCOLOR", (0, 0), (-1, 0), colors.black),
                            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                            ("BOTTOMPADDING", (0, 0), (-1, 0), 12),
                            ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
                            ("ALIGN", (0, 0), (-1, -1), "LEFT"),
                            ("VALIGN", (0, 0), (-1, -1), "TOP")]

    def create_pdf(self, reportData: dict, fileName: str):
        """
        Erzeugt ein PDF mit den Daten des Einsatztagebuchs mit abschließender Seite der
        alarmierten Kräfte
        """

        self.__document.filename = f"{incidentLogPath}{fileName}"

        # --- Title und Header ---
        self.__reportStory.append(Paragraph("Einsatzbericht", self.__styles["Title"]))
        self.__reportStory.append(Spacer(1, 12))

        self.__createHeader(reportData["header"])

        # Erstellung des Einsatztagebuch
        incident_table_data = self.__buildIncidentLogTableData(reportData["incidentLog"])
        incident_table = self.__build_table(incident_table_data, col_widths=[50, 110, 100, 100, 200])
        self.__reportStory.append(incident_table)

        # Eingesetzte Einheiten
        self.__reportStory.append(PageBreak())
        self.__reportStory.append(Paragraph("Alarmierte Einsatzkräfte", self.__styles["Title"]))
        self.__reportStory.append(Spacer(1, 12))

        checkbox_table_data = self.__buildCheckboxTableData(reportData["respondingUnits"])
        checkbox_table = self.__build_table(checkbox_table_data, col_widths=[150, 100, 100, 100, 50])

        self.__reportStory.append(checkbox_table)

        try:
            self.__document.build(self.__reportStory)
        except FileNotFoundError:
            self.__document.filename = f"../{fileName}"
            self.__document.build(self.__reportStory)

    def __createHeader(self, reportHeader: dict):
        header = (
            f"<b>Bericht-Nr.:</b> {reportHeader.get('reportNumber', '')}<br/>"
            f"<b>Alarm-Kategorie:</b> {reportHeader.get('alarmCategory', '')}<br/>"
            f"<b>Alarm-Bereich:</b> {reportHeader.get('alarmArea', '')}<br/>"
            f"<b>Schadensereignis:</b> {reportHeader.get('alarmEvent', '')}<br/>"
            f"<b>Dauer:</b> {reportHeader.get('duration', '')}<br/>"
        )
        self.__reportStory.append(Paragraph(header, self.__styles["Normal"]))
        self.__reportStory.append(Spacer(1, 12))

    def __build_table(self, table_data, col_widths):
        """
        Hilfsfunktion zur Erstellung einer Tabelle.
        """
        table = Table(table_data, colWidths=col_widths)
        table_style = TableStyle(self.__tableStyle)
        table.setStyle(table_style)
        return table

    def __buildIncidentLogTableData(self, report_data: dict):
        """
        Baut die Daten für die Incident-Log-Tabelle zusammen.
        Falls der Text des Eintrags mit Strikethrough versehen sein soll, wird
        dafür der StrikeThroughParagraph verwendet.
        """
        table_data = [["Lfd.Nr.", "Zeitpunkt", "Kategorie", "Absender", "Text"]]

        # Sortiere die Einträge numerisch
        for key in sorted(report_data.keys(), key=lambda x: int(x)):
            entry = report_data[key]
            dateTimeText = entry.get("time", "").replace("\n", "<br/>")
            categoryText = entry.get("category", "").replace("\n", "<br/>")
            senderText = entry.get("reportSender", "").replace("\n", "<br/>")
            reportText = entry.get("reportText", "").replace("\n", "<br/>")
            # Verwende den StrikeThroughParagraph, wenn "striketrough" True ist
            if entry.get("striketrough", False):
                reportTextParagraph = StrikeThroughParagraph(reportText, self.__cellStyle)
            else:
                reportTextParagraph = Paragraph(reportText, self.__cellStyle)

            row = [
                Paragraph(str(key), self.__cellStyle),
                Paragraph(dateTimeText, self.__cellStyle),
                Paragraph(categoryText, self.__cellStyle),
                Paragraph(senderText, self.__cellStyle),
                reportTextParagraph
            ]
            table_data.append(row)
        return table_data

    def __buildCheckboxTableData(self, unit_data: dict):
        """
        Baut die Daten für die Alarmierten Einheiten-Tabelle zusammen.
        """
        table_data = [["Einsatzkraft", "Alarmiert", "EST an", "EST ab", "Anzahl"]]
        for key in sorted(unit_data.keys()):
            entry = unit_data[key]
            unit = entry.get("unit", "")
            alarmTime = entry.get("alarmTime", "")
            arivalSceneTime = entry.get("arivalSceneTime", "")
            departureSceneTime = entry.get("departureSceneTime", "")
            unitCount = entry.get("unitCount", "-")

            row = [Paragraph(unit, self.__cellStyle),
                Paragraph(alarmTime, self.__cellStyle),
                Paragraph(arivalSceneTime, self.__cellStyle),
                Paragraph(departureSceneTime, self.__cellStyle),
                Paragraph(unitCount, self.__cellStyle)]
            table_data.append(row)

        return table_data


# Beispiel zur Verwendung:
if __name__ == "__main__":
    # Incident-Log-Daten für Seite 1
    incident_data = {
        "header": {"reportNumber": "A001",
                   "alarmCategory": "Brand 1",
                   "alarmArea": "Halle B",
                   "alarmEvent": "Brand eines Mülleimers",
                   "duration": "15 min", },
        "incidentLog": {
            "1": {
                "time": "08.02.2025 06:43:00",
                "category": "Lagemeldung",
                "reportSender": "First Responder",
                "reportText": "Lagemeldung lt. Funk. Das ist ein langer Text,\n"
                              "der sich über mehrere Zeilen erstrecken könnte.",
                "striketrough": True
            },
            "2": {
                "time": "08.02.2025 06:48:00",
                "category": "Lagemeldung",
                "reportSender": "C-Dienst",
                "reportText": "Lagemeldung lt. Funk. Hier kann auch ein weiterer längerer Text stehen.",
                "striketrough": False
            },
            "3": {
                "time": "08.02.2025 06:43:00",
                "category": "Lagemeldung",
                "reportSender": "First Responder",
                "reportText": "Lagemeldung lt. Funk. Das ist ein langer Text,\n"
                              "der sich über mehrere Zeilen erstrecken könnte.",
                "striketrough": True
            },
            "4": {
                "time": "08.02.2025 06:48:00",
                "category": "Lagemeldung",
                "reportSender": "C-Dienst",
                "reportText": "Lagemeldung lt. Funk. Hier kann auch ein weiterer längerer Text stehen.",
                "striketrough": False
            },
            "5": {
                "time": "08.02.2025 06:43:00",
                "category": "Lagemeldung",
                "reportSender": "First Responder",
                "reportText": "Lagemeldung lt. Funk. Das ist ein langer Text,\n"
                              "der sich über mehrere Zeilen erstrecken könnte.",
                "striketrough": True
            },
            "6": {
                "time": "08.02.2025 06:48:00",
                "category": "Lagemeldung",
                "reportSender": "C-Dienst",
                "reportText": "Lagemeldung lt. Funk. Hier kann auch ein weiterer längerer Text stehen.",
                "striketrough": False
            },
            "7": {
                "time": "08.02.2025 06:43:00",
                "category": "Lagemeldung",
                "reportSender": "First Responder",
                "reportText": "Lagemeldung lt. Funk. Das ist ein langer Text,\n"
                              "der sich über mehrere Zeilen erstrecken könnte.",
                "striketrough": True
            },
            "8": {
                "time": "08.02.2025 06:48:00",
                "category": "Lagemeldung",
                "reportSender": "C-Dienst",
                "reportText": "Lagemeldung lt. Funk. Hier kann auch ein weiterer längerer Text stehen.",
                "striketrough": False
            },
            "9": {
                "time": "08.02.2025 06:43:00",
                "category": "Lagemeldung",
                "reportSender": "First Responder",
                "reportText": "Lagemeldung lt. Funk. Das ist ein langer Text,\n"
                              "der sich über mehrere Zeilen erstrecken könnte.",
                "striketrough": True
            },
            "10": {
                "time": "08.02.2025 06:48:00",
                "category": "Lagemeldung",
                "reportSender": "C-Dienst",
                "reportText": "Lagemeldung lt. Funk. Hier kann auch ein weiterer längerer Text stehen.",
                "striketrough": False
            },
            "11": {
                "time": "08.02.2025 06:43:00",
                "category": "Lagemeldung",
                "reportSender": "First Responder",
                "reportText": "Lagemeldung lt. Funk. Das ist ein langer Text,\n"
                              "der sich über mehrere Zeilen erstrecken könnte.",
                "striketrough": True
            },
            "12": {
                "time": "08.02.2025 06:43:00",
                "category": "Lagemeldung",
                "reportSender": "First Responder",
                "reportText": "Lagemeldung lt. Funk. Das ist ein langer Text,\n"
                              "der sich über mehrere Zeilen erstrecken könnte.",
                "striketrough": True
            },
            "13": {
                "time": "08.02.2025 06:48:00",
                "category": "Lagemeldung",
                "reportSender": "C-Dienst",
                "reportText": "Lagemeldung lt. Funk. Hier kann auch ein weiterer längerer Text stehen.",
                "striketrough": False
            },
            "14": {
                "time": "08.02.2025 06:43:00",
                "category": "Lagemeldung",
                "reportSender": "First Responder",
                "reportText": "Lagemeldung lt. Funk. Das ist ein langer Text,\n"
                              "der sich über mehrere Zeilen erstrecken könnte.",
                "striketrough": True
            },
            "15": {
                "time": "08.02.2025 06:48:00",
                "category": "Lagemeldung",
                "reportSender": "C-Dienst",
                "reportText": "Lagemeldung lt. Funk. Hier kann auch ein weiterer längerer Text stehen.",
                "striketrough": False
            },
            "16": {
                "time": "08.02.2025 06:43:00",
                "category": "Lagemeldung",
                "reportSender": "First Responder",
                "reportText": "Lagemeldung lt. Funk. Das ist ein langer Text,\n"
                              "der sich über mehrere Zeilen erstrecken könnte.",
                "striketrough": True
            },
            "17": {
                "time": "08.02.2025 06:48:00",
                "category": "Lagemeldung",
                "reportSender": "C-Dienst",
                "reportText": "Lagemeldung lt. Funk. Hier kann auch ein weiterer längerer Text stehen.",
                "striketrough": False
            },
            "18": {
                "time": "08.02.2025 06:43:00",
                "category": "Lagemeldung",
                "reportSender": "First Responder",
                "reportText": "Lagemeldung lt. Funk. Das ist ein langer Text,\n"
                              "der sich über mehrere Zeilen erstrecken könnte.",
                "striketrough": True
            },
            "19": {
                "time": "08.02.2025 06:48:00",
                "category": "Lagemeldung",
                "reportSender": "C-Dienst",
                "reportText": "Lagemeldung lt. Funk. Hier kann auch ein weiterer längerer Text stehen.",
                "striketrough": False
            },
            "20": {
                "time": "08.02.2025 06:43:00",
                "category": "Lagemeldung",
                "reportSender": "First Responder",
                "reportText": "Lagemeldung lt. Funk. Das ist ein langer Text,\n"
                              "der sich über mehrere Zeilen erstrecken könnte.",
                "striketrough": True
            },
            "21": {
                "time": "08.02.2025 06:48:00",
                "category": "Lagemeldung",
                "reportSender": "C-Dienst",
                "reportText": "Lagemeldung lt. Funk. Hier kann auch ein weiterer längerer Text stehen.",
                "striketrough": False
            },
            "22": {
                "time": "08.02.2025 06:43:00",
                "category": "Lagemeldung",
                "reportSender": "First Responder",
                "reportText": "Lagemeldung lt. Funk. Das ist ein langer Text,\n"
                              "der sich über mehrere Zeilen erstrecken könnte.",
                "striketrough": True
            },
            "23": {
                "time": "08.02.2025 06:48:00",
                "category": "Lagemeldung",
                "reportSender": "C-Dienst",
                "reportText": "Lagemeldung lt. Funk. Hier kann auch ein weiterer längerer Text stehen.",
                "striketrough": False
            }
        },
        "respondingUnits": {
            "1": {
                "unit": "Feuerwehr Saarlouis",
                "alarmTime": "20.02.2024 01:25",
                "arivalSceneTime": "20.02.2024 01:35",
                "departureSceneTime": "20.02.2024 05:25",
                "unitCount": "17"
            },
            "2": {
                "unit": "C-Dienst",
                "alarmTime": "20.02.2024 01:25",
                "arivalSceneTime": "20.02.2024 01:35",
                "departureSceneTime": "20.02.2024 05:25",
                "unitCount": "1"
            }
        }
    }

    # Checkbox-Daten für Seite 2

    pdf_file_path = "einsatzbericht_mit_checkbox_tabelle.pdf"  # Pfad anpassen
    IncidentLogReportGenerator().create_pdf(incident_data, pdf_file_path)
