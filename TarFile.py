#########################################################################################################
# Nom du script :       Save_Blob_Azure_Script.py                                                       #
# Auteur :              Mathieu Fabri                                                                   #
# Date de création :    2020-04                                                                         #
# Version :             1.0                                                                             #
# Langage :             Python                                                                          #
# Description :         Script pour sauvegarder les fichiers sur Azure Blob                             #
# License :             GPL3 - https://github.com/Altins752/Save_Blob_Azure_Script/blob/main/LICENSE    #
# GitHub :              https://github.com/Altins752/Save_Blob_Azure_Script                             #
#########################################################################################################

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