#!/usr/bin/python3
import os, datetime, shutil
from dumpBDD import DumpMysql
from TarFile import creatArchive
from fileName import fileDelete
from datetime import datetime, timedelta
from saveBlob import importBlob

try:
    shutil.copytree("/var/www/html/", "./bckp_wp/siteWP")

    bckpFolder = DumpMysql("admin", "admin")
    archiveName = creatArchive(bckpFolder)
    shutil.move(archiveName, f"./bckp_blob/{archiveName}")
    print(f"\nLe fichier {archiveName} a été créer\n")

    importBlob(archiveName)

    oldArchive = fileDelete("bckp_wp","tar.gz")
    os.remove(f"./bckp_blob/{oldArchive}")
    print(f"Le fichier {oldArchive} a été suprimé")
  
except Exception as ex:
    print('Exception:')
    print(ex)