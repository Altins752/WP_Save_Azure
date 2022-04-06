import os, datetime
from dumpBDD import DumpMysql
from TarFile import creatArchive
from fileName import fileDelete
from datetime import datetime, timedelta
from saveBlob import importBlob

try:
    os.system("mkdir bckp_wp")
    os.system("cp -rf /var/www/html/ ./bckp_wp")
    os.system("mv ./bckp_wp/html ./bckp_wp/siteWP")

    bckpFolder = DumpMysql("admin", "admin")
    archiveName = creatArchive(bckpFolder)
    os.system(f"mv ./{archiveName} ./bckp_blob")
    print(f"Le fichier {archiveName} a été créer")

    oldArchive = fileDelete("bckp_wp","tar.gz")
    os.system(f"rm -rf {oldArchive}")
    print(f"Le fichier {oldArchive} a été suprimé")

    importBlob(archiveName)


  
except Exception as ex:
    print('Exception:')
    print(ex)