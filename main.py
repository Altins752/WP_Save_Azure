#!/usr/bin/python3
import os, datetime, shutil, configparser, syslog
from dumpBDD import DumpMysql
from TarFile import creatArchive
from fileName import fileDelete
from datetime import datetime, timedelta
from saveBlob import importBlob, deletBlob

# définition des variables avec le fichier de configuration
config = configparser.RawConfigParser() 
config.read('config')

idBDD = config.get('BDD', 'bddid')
mdpBDD = config.get('BDD', 'bddmdp')
nameBDD = config.get('BDD', 'bddname')

cnct_str = config.get('AZURE', 'connect_string')
ctnr_name = config.get('AZURE', 'container_name')

folder_path_bckp = config.get('FILES', 'folder_path')
folder_path_local_bckp = config.get('FILES', 'local_Backup')
jrs = config.get('FILES', 'day_retention')

#conversion de la variable jrs en int
jrs = int(jrs)

# appels des différentes fonction pour effectuer la sauvegarde
try:
    # création de l'archive à sauvegarder
    shutil.copytree(folder_path_bckp, "./bckp_wp_temp/siteWP")

    DumpMysql(idBDD, mdpBDD, nameBDD, folder_path_local_bckp)
    archiveName = creatArchive(folder_path_local_bckp)
    shutil.move(archiveName, f"{folder_path_local_bckp}{archiveName}")

    print(f"\nLe fichier {archiveName} a été créer\n")

    #imports de l'archive vers le container Azure
    importBlob(archiveName, folder_path_local_bckp, cnct_str, ctnr_name)

    # supression de l'archive dans le containers Blob suivant le nombre de jours configuré
    oldArchive = fileDelete("bckp","tar.gz", jrs)
    error=deletBlob(oldArchive, cnct_str, ctnr_name)

    if error == 1 :
        syslog.syslog("Ancien blob non suprimé car inexistant - le script est quand même aller au bout")
    else:   
        syslog.syslog("Tout s'est bien déroulé")

except Exception as ex:
    print('Exception:')
    print(ex)