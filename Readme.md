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

python table_extraction.py -i <input_file> -o <output_path>


- `<input_file>`: Pfad zur Eingabe-PDF-Datei.
- `<output_path>`: Pfad zum Ausgabeverzeichnis, in dem die CSV-Dateien gespeichert werden.

## Beispiel

python table_extraction.py -i input.pdf -o output/


Dieser Befehl extrahiert Tabellen aus der Datei "input.pdf" und speichert die CSV-Dateien im Verzeichnis "output/".

## Lizenz

Dieses Skript steht unter der MIT-Lizenz. Weitere Informationen finden Sie in der [Lizenzdatei](LICENSE).
