# KI-Generiert - Anpassung fehlt

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Paragraph
from reportlab.platypus import (
    SimpleDocTemplate,
    Table,
    TableStyle,
    Spacer,
    PageBreak
)


# Benutzerdefinierter Paragraph, der einen Strikethrough-Effekt über die gesamte Zeile zeichnet.
class StrikeThroughParagraph(Paragraph):
    def __init__(self, text, style, strike=False):
        self.strike = strike
        super().__init__(text, style)

    def draw(self):
        # Zuerst den normalen Paragraphen zeichnen
        super().draw()
        # Falls der Strikethrough-Effekt gewünscht ist und Zeilen vorhanden sind:
        if self.strike and hasattr(self, 'blPara') and self.blPara:
            # Iteriere über alle Zeilen (FragLine-Objekte) des formatierten Paragraphen.
            for i, frag in enumerate(self.blPara.lines):
                # Versuche den Text der FragLine auszulesen, falls vorhanden.
                #line_text = getattr(frag, 'text', str(frag))
                # Anstatt die Breite des Textes zu berechnen, verwenden wir die ganze verfügbare Breite.
                line_width = self.width  # Ganze Breite des Paragraphen
                # Berechne eine y-Position in der Mitte der jeweiligen Zeile.
                y = self.height - (i + 0.5) * self.style.leading
                self.canv.setLineWidth(0.5)
                self.canv.line(0, y, line_width, y)


class EinsatzberichtPDFGenerator:
    @staticmethod
    def create_pdf(report_data: dict, checkbox_data: dict, pdf_path: str):
        """
        Erzeugt ein PDF mit zwei Seiten:
        - Seite 1: Incident-Log-Daten. Falls in einem Eintrag "striketrough" True ist,
          wird der Text mit einem Strikethrough-Effekt über die gesamte Zeile angezeigt.
        - Seite 2: Eine Tabelle mit Einsatzkräften und einem einfachen Checkbox-Symbol
          ('X' bei True, ' ' bei False), dargestellt in tabellarischer Form.
        """
        doc = SimpleDocTemplate(pdf_path, pagesize=A4)
        story = []
        styles = getSampleStyleSheet()

        # ParagraphStyle für Tabellenzellen (linksbündig)
        cell_style = ParagraphStyle(
            name="CellStyle",
            parent=styles["BodyText"],
            alignment=0,  # linksbündig
            leading=12,
            spaceAfter=4
        )

        # --- Seite 1: Incident-Log / Hauptinhalt ---
        story.append(Paragraph("Einsatzbericht", styles["Title"]))
        story.append(Spacer(1, 12))

        # Allgemeine Informationen
        gen_info = (
            f"<b>Bericht-Nr.:</b> {report_data.get('reportNumber', '')}<br/>"
            f"<b>Alarm-Kategorie:</b> {report_data.get('alarmCategory', '')}<br/>"
            f"<b>Alarm-Bereich:</b> {report_data.get('alarmArea', '')}<br/>"
            f"<b>Schadensereignis:</b> {report_data.get('alarmEvent', '')}<br/>"
            f"<b>Dauer:</b> {report_data.get('duration', '')}<br/>"
        )
        story.append(Paragraph(gen_info, styles["Normal"]))
        story.append(Spacer(1, 12))

        # Erstellung der Incident-Log-Tabelle
        incident_table_data = EinsatzberichtPDFGenerator._build_incident_log_table_data(report_data, cell_style)
        incident_table = EinsatzberichtPDFGenerator._build_table(
            incident_table_data,
            col_widths=[50, 110, 100, 100, 200],
            style_cmds=[
                ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.black),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("BOTTOMPADDING", (0, 0), (-1, 0), 12),
                ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
                ("ALIGN", (0, 0), (-1, -1), "LEFT"),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ]
        )
        story.append(incident_table)

        # --- Seite 2: Checkbox-Tabelle für Einsatzkräfte ---
        story.append(PageBreak())
        story.append(Paragraph("Einsatzkräfte", styles["Heading2"]))
        story.append(Spacer(1, 12))

        checkbox_table_data = EinsatzberichtPDFGenerator._build_checkbox_table_data(checkbox_data)
        checkbox_table = EinsatzberichtPDFGenerator._build_table(
            checkbox_table_data,
            col_widths=[100, 50, 100],
            style_cmds=[
                ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.black),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("ALIGN", (0, 0), (-1, -1), "LEFT"),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
                ("LEFTPADDING", (0, 0), (-1, -1), 5),
                ("RIGHTPADDING", (0, 0), (-1, -1), 5),
                ("TOPPADDING", (0, 0), (-1, -1), 3),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
            ]
        )
        story.append(checkbox_table)

        # PDF erstellen
        doc.build(story)
        print(f"PDF wurde erfolgreich unter {pdf_path} gespeichert!")

    @staticmethod
    def _build_table(table_data, col_widths, style_cmds):
        """
        Hilfsfunktion zur Erstellung einer Tabelle.
        """
        table = Table(table_data, colWidths=col_widths)
        table_style = TableStyle(style_cmds)
        table.setStyle(table_style)
        return table

    @staticmethod
    def _build_incident_log_table_data(report_data: dict, cell_style: ParagraphStyle):
        """
        Baut die Daten für die Incident-Log-Tabelle zusammen.
        Falls der Text des Eintrags mit Strikethrough versehen sein soll, wird
        dafür der StrikeThroughParagraph verwendet.
        """
        table_data = [["Lfd.Nr.", "Zeitpunkt", "Kategorie", "Absender", "Text"]]
        incident_log = report_data.get("incidentLog", {})

        # Sortiere die Einträge numerisch
        for key in sorted(incident_log.keys(), key=lambda x: int(x)):
            entry = incident_log[key]
            time_text = entry.get("time", "").replace("\n", "<br/>")
            cat_text = entry.get("category", "").replace("\n", "<br/>")
            sender_text = entry.get("reportSender", "").replace("\n", "<br/>")
            rep_text = entry.get("reportText", "").replace("\n", "<br/>")
            # Verwende den StrikeThroughParagraph, wenn "striketrough" True ist
            if entry.get("striketrough", False):
                text_para = StrikeThroughParagraph(rep_text, cell_style, strike=True)
            else:
                text_para = Paragraph(rep_text, cell_style)

            row = [
                Paragraph(str(key), cell_style),
                Paragraph(time_text, cell_style),
                Paragraph(cat_text, cell_style),
                Paragraph(sender_text, cell_style),
                text_para
            ]
            table_data.append(row)
        return table_data

    @staticmethod
    def _build_checkbox_table_data(checkbox_data: dict):
        """
        Baut die Daten für die Checkbox-Tabelle der Einsatzkräfte zusammen.
        Das Format der Checkbox-Daten ist ein Dictionary, in dem der Key
        die Einsatzkraft repräsentiert und der Value ein Array mit [status, alarmiert] ist.
        """
        table_data = [["Einsatzkraft", "Status", "Alarmiert"]]
        for kraft, values in checkbox_data.items():
            status = values[0]
            checkbox_symbol = "X" if status else " "
            table_data.append([kraft, checkbox_symbol, values[1]])
        return table_data


# Beispiel zur Verwendung:
if __name__ == "__main__":
    # Incident-Log-Daten für Seite 1
    incident_data = {
        "reportNumber": "A001",
        "alarmCategory": "Brand 1",
        "alarmArea": "Halle B",
        "alarmEvent": "Brand eines Mülleimers",
        "duration": "15 min",
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



        }
    }

    # Checkbox-Daten für Seite 2
    additional_checkbox_data = {
        "C-Dienst": [True, "08.02.2025 06:45"],
        "B-Dienst": [False, ""],
        "A-Dienst": [False, ""],
        "Angriffstrupp": [True, "08.02.2025 06:45"],
        "Wassertrupp": [True, "08.02.2025 06:45"],
        "Schlauchtrupp": [False, ""],
        "Melder": [False, ""],
        "Maschinist": [True, "08.02.2025 06:45"],
        "First Responder": [False, ""],
        "1/55": [True, "08.02.2025 06:45"],
        "1/48": [True, "08.02.2025 06:45"],
        "1/29": [False, ""],
        "1/83": [False, ""],
        "1/61": [False, ""],
        "1/18": [False, ""],
        "1/10": [False, ""],
        "Mot-Streife": [False, ""]
    }

    pdf_file_path = "einsatzbericht_mit_checkbox_tabelle.pdf"  # Pfad anpassen
    EinsatzberichtPDFGenerator.create_pdf(incident_data, additional_checkbox_data, pdf_file_path)
