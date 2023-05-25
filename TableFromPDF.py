#!/usr/bin/env python
# encoding: utf-8

# Author: Markus Saalmann
# Das Script ermittelt aus einem PFD-File Tabellen Objekte und exportiert diese in Export Dateien
#
#-----------------------------------------------------------------------------------------------------------------------------------------

#Importe für den SMTP Versand
import json #Lesen der Konfiguration
import time #Sleeper
import argparse #ARGS parsen
import pandas as pd
import tabula
import os



# Project defined imports
#-----------------------------
#Konfiguration lesen
f = open('config.json')
config = json.load(f)

import sys
sys.path.append(config['LIB_PATH']) 
from libCore.libTrace import Trace #Bibliothek für ein zentrales Tracing
from libCore.libHelper import * #OS Hilfsfunktionen

#-Funktionen-------------------------------------------------------------------------------------------------------------------------------


#-Work-------------------------------------------------------------------------------------------------------------------------------------
def doWork(input_file, output_path, export_format, file_prefix):
    Trace ('Start Extraktion Work...')

    #-Lese PDF File------------------------------------
    tables = tabula.read_pdf(input_file, pages='all')  
    Trace (f'...{ len(tables)} Tabellen wurden ermittelt...','D')
    
    for tableindex, df in enumerate(tables):
        Trace(f'...Ermittlung Tabelle {tableindex+1}...')
        
        df.columns = df.iloc[0]
        df = df[1:]
        
        _filename  = f'{file_prefix}{tableindex + 1}'
        _outputFile = os.path.join(output_path,_filename )
        Trace(f'...schreibe Datei {_outputFile}...')
        try:
            if export_format =='XLSX':
                 _outputFile +='.xlsx'
                 df.to_excel(_outputFile)
            elif export_format =='HTML':
                 _outputFile +='.html'
                 df.to_html(_outputFile)
            elif export_format =='XML':
                 _outputFile +='.xml'
                 df.columns = df.columns.str.replace(' ', '_', regex=True).str.replace('[^\w\s]', '', regex=True)
                 df.to_xml(_outputFile)
            elif export_format =='JSON':
                 _outputFile +='.json'
                 with open(_outputFile, 'w') as file:
                    df.to_json(file, force_ascii=False, orient='table')
            else:
                _outputFile +='.csv'
                df.to_csv(_outputFile,sep='|')
        except Exception as e: 
            Trace(f'{e}','E')
        else:
            Trace(f'...successful!')
        
    
   
#-MAIN-------------------------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    Trace().activateTrace(InformationTypes=config['LOG_InformationTypes'],WriteOnlyToLogFile=config['LOG_WriteOnlyToLogFile'], LogFilePath=config['LOG_PATH'])
    Trace(f"********* APP: {config['APP_NAME']} ******** Version: {config['APP_VERSION']} ***************")
    
    #ARG Parser initialisieren
    #---------------------------------
    parser = argparse.ArgumentParser(
        prog = config['APP_NAME'],
        description = '''Das Script ermittelt aus einem PDF File alle vorhandenen Tabellen und erzeugt entsprechende CSV-Ausgabedateien je Tabelle ''')
    parser.add_argument('-i', dest='PFDFile', required = True, help='Pfad inkl. Dateinamen der entsprechenden PDF Datei' )
    parser.add_argument('-o', dest='OutputPath', required = True, help='Pfad in den die Exportdateien geschrieben werden sollen' )
    parser.add_argument('-f', dest='ExportFormat', required = False,  help='Folgende Export-Formate sind möglich (csv, xlsx, html, json, xml). Default=csv' )
    parser.add_argument('-p', dest='OutputFilePrefix', required = False,  help='Praefix Filename für die Export-Files gefolgt von der identifizierten Tabellen-ID' )
    
    args = parser.parse_args()
    
    _INPUT_FILE = args.PFDFile
    _OUTPUT_PATH = args.OutputPath
    _EXPORT_FORMAT = str(args.ExportFormat).upper()
    _EXPORT_FILE_PREFIX = args.OutputFilePrefix
    if not _EXPORT_FILE_PREFIX:
        _EXPORT_FILE_PREFIX = 'expTable'
    
    if _EXPORT_FORMAT=='NONE':
        _EXPORT_FORMAT='CSV'
        
    #-Prüfung Argumente-------------------------------------------------
    Trace(f'Input-File: {_INPUT_FILE}','I')
    if not OScheckDir(_INPUT_FILE):
        Trace('PDF File not exists','E')
        sys.exit()
    else:
        Trace('Check File successful!','I')
    
    Trace(f'Output-Path: {_OUTPUT_PATH}','I')
    if OScheckDir(_OUTPUT_PATH):
        Trace('Check path successful!')
    else:
        Trace('Path not exists!','W')
        OSmakeDir(_OUTPUT_PATH)
        Trace('Path generated!','I')
    
    Trace(f'FilePraefix: {_EXPORT_FILE_PREFIX}','I')
    
    Trace(f'Export-Format: {_EXPORT_FORMAT}','I')
    if _EXPORT_FORMAT not in ('CSV','XLSX','HTML','XML','JSON'):
        Trace(f'Export-Format not allowed!','F')
        sys.exit()
    
    doWork(input_file=_INPUT_FILE, output_path=_OUTPUT_PATH, export_format=_EXPORT_FORMAT, file_prefix= _EXPORT_FILE_PREFIX)
    
    
    
    