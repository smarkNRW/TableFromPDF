# PDF Table Extraction

Dieses Skript ermittelt aus einem PDF-File Tabellen-Objekte und exportiert sie in separate CSV-Dateien.

## Voraussetzungen

- Python 3.x
- Pandas-Bibliothek
- Tabula-Bibliothek

## Installation

1. Klonen Sie das Repository oder laden Sie das Skript herunter.
2. Installieren Sie die erforderlichen Bibliotheken mit dem Befehl `pip install -r requirements.txt`.

## Verwendung

Führen Sie das Skript mit den folgenden Parametern aus:

python script.py -i <PDF-Datei> -o <Ausgabepfad> [-f <Exportformat>] [-p <Dateipräfix>]

## Argumente

- i <PDF-Datei>: Pfad zur Eingabe-PDF-Datei (erforderlich).
- o <Ausgabepfad>: Pfad, in dem die Exportdateien gespeichert werden sollen (erforderlich).
- f <Exportformat> (optional): Das Exportformat für die Tabellen. Mögliche Werte: csv, xlsx, html, xml, json. Standardmäßig wird CSV verwendet.
- p <Dateipräfix> (optional): Das Dateipräfix für die Exportdateien gefolgt von der identifizierten Tabellen-ID. Standardmäßig wird "expTable" verwendet.

## Beispiel

python script.py -i input.pdf -o output -f xlsx -p table

Dieses Beispiel extrahiert Tabellen aus der Datei "input.pdf" und speichert sie als XLSX-Dateien mit dem Präfix "table" im Ordner "output".

python script.py -i input.pdf -o output -f csv

Dieses Beispiel extrahiert Tabellen aus der Datei "input.pdf" und speichert sie als CSV-Dateien im Ordner "output".

## Lizenz

Dieses Skript steht unter der MIT-Lizenz. Weitere Informationen finden Sie in der [Lizenzdatei](LICENSE).
