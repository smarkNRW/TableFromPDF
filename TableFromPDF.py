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
def doWork(input_file, output_path):
    Trace ('Start Extraktion Work...')

    #-Lese PDF File------------------------------------
    tables = tabula.read_pdf(input_file, pages='all')  
    Trace (f'...{ len(tables)} Tabellen wurden ermittelt...','D')
    tableindex=0  
    while tableindex < len(tables):
        Trace(f'...Ermittlung Tabelle {tableindex+1}...')
        df = tables[tableindex]
        df.columns = df.iloc[0]
        df = df[1:]
        tableindex +=1
        _filesname = 'expTable'+str(tableindex)+'csv'
        _outputFile = os.path.join(output_path,_filesname)
        Trace(f'...schreibe Datei {_outputFile}...')
        try:
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
    parser.add_argument('-i', dest='PFDFile', required = True, )
    parser.add_argument('-o', dest='OutputPath', required = True, )
    args = parser.parse_args()
    
    _INPUT_FILE = args.PFDFile
    _OUTPUT_PATH = args.OutputPath
    
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
    
    doWork(input_file=_INPUT_FILE, output_path=_OUTPUT_PATH)
    
    
    
    