#!/usr/bin/python3
import tarfile, shutil
from fileName import fileCreate

# fonction pour créer l'archive à sauvegarder sur Azure blob
def creatArchive(foldername):
    archivename = fileCreate("bckp","tar.gz")
    backup = tarfile.open(archivename, mode='w:gz')
    backup.add(foldername)
    backup.close()
    shutil.rmtree("bckp_wp_temp")
    return archivename