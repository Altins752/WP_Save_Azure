#!/usr/bin/python3
import os
from fileName import fileCreate

# fonction pour réaliser un dump de la base de donnée définis dans le fichier de configuration
def DumpMysql(username, password, bddname, foldername):
    filename = fileCreate("wp_bdd_bckp", "sql")
    filename = f"{foldername}/{filename}"
    os.system(f"mysqldump -u {username} -p{password} {bddname} > {filename}")
    return foldername
