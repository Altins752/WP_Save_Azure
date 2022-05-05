#!/usr/bin/python3
import os, datetime, shutil, configparser, syslog, logging
import logging.config
from pprint import pprint
from dumpBDD import DumpMysql
from TarFile import creatArchive
from fileName import fileDelete
from datetime import datetime, timedelta
from saveBlob import importBlob, deletBlob

# Configuration logging
logging.config.fileConfig('logging.conf')

myLog = logging.getLogger('SaveBlobAzureScript')

myLog.info("Début du script")

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



# appels des différentes fonction pour effectuer la sauvegarde
try:
    #conversion de la variable jrs en int
    jrs = int(jrs)

    # Controle existance dossier bckp local
    if not os.path.exists(folder_path_local_bckp):
        myLog.error("Le dossier de sauvegarde local n'existe pas ou est inaccessible")
        myLog.info("arrêt du script")
        exit()

    # création de l'archive à sauvegarder
    myLog.info("Création de l'archive à sauvegarder")

    shutil.copytree(folder_path_bckp, "./bckp_wp_temp/siteWP")

    myLog.info(f"Dump de la base de donnée {nameBDD}")

    DumpMysql(idBDD, mdpBDD, nameBDD, folder_path_local_bckp)
    archiveName = creatArchive(folder_path_local_bckp)
    shutil.move(archiveName, f"{folder_path_local_bckp}{archiveName}")

    myLog.info("Création de l'archive terminer sans erreur")

    myLog.info("Téléversement de l'archive sur Azure Blob")
    #imports de l'archive vers le container Azure
    importBlob(archiveName, folder_path_local_bckp, cnct_str, ctnr_name)

    myLog.info("Téléversement terminé")

    myLog.info("Suppression de l'ancienne archive sur Azure Blob")
    # supression de l'archive dans le containers Blob suivant le nombre de jours configuré
    oldArchive = fileDelete("bckp","tar.gz", jrs)
    error=deletBlob(oldArchive, cnct_str, ctnr_name)

# Gestion de l'erreur en cas d'ancien blob non existant mais non bloquant pour la finalisation du Script
    if error == 1 :
        myLog.warning("Ancien blob non suprimé car inexistant - le script est quand même aller au bout")
    else:   
        myLog.info("Tout s'est bien passé")

# exception pour gérer les erreurs
except FileNotFoundError as ex:
    myLog.error("Le chemin des fichier a sauvegarder est inconnue ou inaccessible")
    myLog.info("arrêt du script")
    exit()

except ValueError as ex:
    myLog.error("La valeur de la variable jrs doit être un nombre entier (uniquement des caractères alphanumérique sans décimaux)")
    myLog.info("arrêt du script")
    exit()

except Exception as ex:
    myLog.error("Une erreur inconnue est survenue")
    myLog.debug(ex)
    myLog.info("arrêt du script")
    exit()