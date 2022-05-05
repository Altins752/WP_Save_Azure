#!/usr/bin/python3
import os, shutil, logging, sys
import logging.config
from fileName import fileCreate

# Configuration logging
logging.config.fileConfig('logging.conf')

myLog = logging.getLogger('SaveBlobAzureScript')

# fonction pour réaliser un dump de la base de donnée définis dans le fichier de configuration
def DumpMysql(username, password, bddname, foldername):
    filename = fileCreate("wp_bdd_bckp", "sql")
    filename = f"{foldername}/{filename}"
    tests = os.system(f"mysqldump -u {username} -p{password} {bddname} > {filename}")

# Vérification du bon déroulement du dump    
    if tests == 0:
        myLog.info("Dump réalisé avec succés")
        return foldername
    else:
        myLog.error("Erreur lors du dump. Vérifiez les paramètres de connexion et si la base de donnée est bien accessible")
        myLog.info("arrêt du script")
        shutil.rmtree("./bckp_wp_temp")
        sys.exit(2)
        exit()
