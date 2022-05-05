#!/usr/bin/python3
import os, syslog, shutil
from fileName import fileCreate

# fonction pour réaliser un dump de la base de donnée définis dans le fichier de configuration
def DumpMysql(username, password, bddname, foldername):
    filename = fileCreate("wp_bdd_bckp", "sql")
    filename = f"{foldername}/{filename}"
    tests = os.system(f"mysqldump -u {username} -p{password} {bddname} > {filename}")
    
    if tests == 0:
        print("Dump réalisé")
        return foldername
    else:
        syslog.syslog("Erreur lors du dump. Vérifiez les paramètres de connexion et si la base de donnée est bien accessible")
        syslog.syslog("arrêt du script")
        shutil.rmtree("./bckp_wp_temp")
        exit()
