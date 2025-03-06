# IncidentLog – Incident Logging & Alert Management Application

This project is a utility for managing incident reports and alert notifications through a graphical user interface built with PyQt6. It supports capturing, editing, and reviewing incident log entries as well as generating PDF reports using ReportLab. In addition, the project provides dedicated modules for signal management, custom widgets, layouts, and other utility functions.

## Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation and Execution](#installation-and-execution)
- [Configuration](#configuration)
- [License](#license)

## Features

- **Incident Logging:** Create new incident entries via a dedicated GUI.
- **Alert Management:** Manage internal and external emergency units.
- **PDF Reports:** Generate PDF incident reports using ReportLab.
- **Custom Widgets & Layouts:** Modular input fields, tables, and button layouts.
- **Signal Management:** Central signal management using PyQt signals (via the `signalManager`).
- **Error Logging:** Any errors are logged to a file (`log.txt`).
- **Dynamic Styling:** External stylesheets and color themes are loaded via JSON configuration files.

## Project Structure

The project is organized into several modules and subfolders:

- **globals.py:**  
  Loads global configuration data (such as categories, report senders, icons, etc.) and the color theme from JSON files.

- **start.py:**  
  Bootstraps the application, loads the stylesheets, and initializes the GUI components.

- **utilityClasses:**  
  Contains classes for general functionalities:
  - `signalManager.py`: Central signal management.
  - `dataManager.py`: (Placeholder – reserved for future enhancements.)
  - `layoutSpacer.py`: Provides layout spacers for flexible GUI design.
  - `shadowEffect.py`: Applies shadow effects to widgets.
  - `getTimeStamp.py`: Retrieves the current timestamp (including the user's full name via win32api).
  - `customMessageBox.py`: Customized message boxes for information and confirmation dialogs.
  - `reportGenerator`: Module to generate the incident log PDF (including support for strike-through text when necessary).
  - `writeErrorToLogFile.py`: Logs errors to a file.

- **elementsGui:**  
  Contains all GUI components organized into:
  - **inputWidgets:** Customizable input fields (e.g., for time, text, or numeric input).
  - **buttons:** Standardized icon buttons (e.g., clock button, icon button).
  - **layouts:** Predefined layouts for different forms and rows – including layouts for adding and editing incident entries and unit information.
  - **labels:** Label widgets, including those with special effects (e.g., OutlineTitleLabel).
  - **windows:** Main application window (`IncidentLogWindow`) and modal dialogs (e.g., AddEntryWindow, ChangeEntryWindow, AddRespondingUnitWindow, ChangeRespondingUnitsWindow).
  - **groupBoxes:** Grouped layouts for headers, tables, and buttons.
  - **tableWidget:** Classes for displaying and editing tables (e.g., IncidentLogTableWidget, RespondingUnitsTableWidget).

- **ablagen:**  
  Contains alternative versions/backups of the global configuration.

## Prerequisites

- **Python 3.6+**
- **PyQt6:** For the graphical interface  
  Install via pip:
  ```bash
  pip install PyQt6
  ```
ReportLab: For PDF report generation
Install via pip:
  ```bash
  pip install reportlab
  pywin32: For accessing win32api (only necessary on Windows)
  ```
Install via pip:
  ```bash
  pip install pywin32
  ```
## Installation and Execution
Clone the Repository:

  ```bash
  git clone https://github.com/YOUR_USERNAME/NeuesDienstprogramm.git
  cd NeuesDienstprogramm/IncidentLog
  ```
Install Dependencies:

  ```bash
  pip install -r requirements.txt
  Note: If no requirements.txt is provided, ensure that PyQt6, ReportLab, and pywin32 are installed manually.
  ```
Start the Application:

  ```bash
  python IncidentLog/start.py
  ```

## Configuration
Global Variables & Color Theme:
Configuration is loaded from JSON files located in the json folder (e.g., global.json) and the styles folder (e.g., colorTheme.json).
Changes to these files can adjust both the behavior and appearance of the application.

Stylesheets:
All QSS (Qt Style Sheets) files are located in the 'styles' folder. They are merged at startup and dynamically adjusted based on the defined color theme.

## License
This project is licensed under the MIT License.