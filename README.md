# Automated Log Analysis System

A desktop application for scanning and analyzing log files to detect errors and provide solutions using a mapping table. Built for use in industrial and IT environments.

---

##  Features

- Manual or automatic keyword-based log analysis
- Supports multiple `.json` log files
- Help function to display cause and corrective actions for known error codes
- GUI built with PyQt5
- Offline, fast, and simple to use

---

##  How It Works

###  Log File Analysis
- **Manual Mode:** Enter one or more keywords (comma-separated) to search within selected `.json` log files.
- **Automatic Mode:** Automatically scans for a default keyword (e.g., `EALM`).
- Results are displayed in a table showing:
  - File name
  - Line number
  - Matching line content
  - Click to view full log file with highlight

###  Help Function
- Enter an error code in the Help section.
- The system looks it up in the `mapping_table.csv`.
- If found, it displays:
  - **Cause** of the error
  - **Corrective actions**
- If not found, shows: `"No matched error code"`

---

##  Tech Stack

| Component       | Technology       |
|----------------|------------------|
| Language        | Python 3         |
| GUI             | PyQt5            |
| File Handling   | `os`, `pathlib`  |
| Pattern Matching| `re` (regex)     |
| Log File Format | `.json`          |
| Mapping Table   | `.csv` (Excel-compatible) |

---


## Example UI Screens
### Mode	Description
 Search File	  | Choose and scan one or more .log files
 Manual Search	|Input custom keywords
 Auto Search	  |Use default Word (e.g., EALM)
 Help	Input     |error code and retrieve cause/solution

## Development Timeline
### Month	Milestone
March	| Planning & Requirements Gathering
April	| High-Level and Low-Level Design
May	  | Development & Testing
June	| Final Integration, Documentation, Demo

## Team
Name	                 | Student ID
Aleksandr Atakov		   | 202412042
Aleksandr Avdeev		   | 202412027
Muhammad Mubashir		   | 202412120
Rachel Grajeda Angulo	 | 202412182

## Testing
 Manual log testing with APRO’s sample logs

 Unit testing on keyword detection and Help module

 Integration testing for UI navigation and file handling


### License
This project is for academic and non-commercial use. For deployment in industrial settings or licensing, contact the developers or APRO directly.

## Acknowledgments
Professor Lim We Cheol – Project Supervisor

APRO – Industry partner, advisor, and data provider

