#!/usr/bin/env python3
import os
import sys
import tkinter as tk


def collect_files(folder_path):
    """Durchsucht rekursiv den Ordner nach .py Dateien, liest deren Inhalt und
    erstellt einen zusammengefügten Text mit Titelleisten und Trennlinien."""
    output = ""
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                # Absoluter Dateipfad
                abs_path = os.path.abspath(file_path)
                try:
                    with open(file_path, 'r', encoding="utf-8") as f:
                        content = f.read()
                except Exception as e:
                    content = f"Fehler beim Lesen der Datei: {e}"
                # Zusammenfügen: Titelzeile, Inhalt und Trennlinie
                output += f"‘{abs_path}’\n"
                output += content + "\n"
                output += "______________\n"
    return output


def copy_to_clipboard(text):
    """Kopiert den gegebenen Text in die Zwischenablage unter Verwendung von tkinter."""
    try:
        # Tkinter initialisieren, ohne ein Fenster anzuzeigen
        root = tk.Tk()
        root.withdraw()
        root.clipboard_clear()
        root.clipboard_append(text)
        # Wichtiger Hinweis: update() bewirkt, dass der Inhalt auch nach
        # Schließen des Fensters in der Zwischenablage bleibt.
        root.update()
        root.destroy()
        print("Der zusammengeführte Quellcode wurde in die Zwischenablage kopiert.")
    except Exception as e:
        print("Fehler beim Kopieren in die Zwischenablage:", e)
        print("Stattdessen wird der zusammengeführte Quellcode hier ausgegeben:")
        print(text)


if __name__ == '__main__':

    folder_path = "D:\\Python\\Projekte\\AAO\\Neue AAO\\GitHub\\NeuesDienstprogramm\\IncidentLog\\IncidentLog"

    entire_code = collect_files(folder_path)
    print(entire_code)
    copy_to_clipboard(entire_code)
