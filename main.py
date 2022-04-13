#!/usr/bin/python3
import os, datetime, shutil, configparser
from dumpBDD import DumpMysql
from TarFile import creatArchive
from fileName import fileDelete
from datetime import datetime, timedelta
from saveBlob import importBlob, deletBlob



config = configparser.RawConfigParser() 
config.read('config')

idBDD = config.get('BDD', 'id')
mdpBDD = config.get('BDD', 'mdp')

cnct_str = config.get('AZURE', 'connect_string')
ctnr_name = config.get('AZURE', 'container_name')

try:
    shutil.copytree("/var/www/html/", "./bckp_wp/siteWP")

    bckpFolder = DumpMysql(idBDD, mdpBDD)
    archiveName = creatArchive(bckpFolder)
    shutil.move(archiveName, f"./bckp_blob/{archiveName}")
    print(f"\nLe fichier {archiveName} a été créer\n")

    importBlob(archiveName, cnct_str, ctnr_name)


    oldArchive = fileDelete("bckp_wp","tar.gz")
    # os.remove(f"./bckp_blob/{oldArchive}")
    # print(f"Le fichier {oldArchive} a été suprimé")
   
    deletBlob(oldArchive, cnct_str, ctnr_name)

except Exception as ex:
    print('Exception:')
    print(ex)