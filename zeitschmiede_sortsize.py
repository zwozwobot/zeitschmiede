import os
import shutil
import sys

if len(sys.argv) != 4:
    print("Anzahl der Argumente stimmt nicht! 1: zu sortierendes Verzeichnis; 2: Zielordner; 3: Dateigröße für Cut")
    exit()

vonWo = sys.argv[1]
Wohin = sys.argv[2]
WieGross = int(sys.argv[3])

#macht eine Liste aller Dateien/Ordner im genannten Verzeichnis
filesAndDirectories = os.listdir(vonWo) 

#ruft alle Dateien/Ordner im o.g. Verzeichnis einzeln auf
for item in filesAndDirectories: 
    #schreibt in statinfo diverse Metadaten der aufgerufenen Datei/Ordner
    item = vonWo + "/" + item
    statinfo = os.stat(item) 
    #selektiert nach Dateigröße und Dateityp
    if os.path.isfile(item) and statinfo.st_size > WieGross and item.endswith('jpg'): 
        #kopiert selektierte Dateien in einen neuen Ordner
        shutil.copy2(item, Wohin) 


 



