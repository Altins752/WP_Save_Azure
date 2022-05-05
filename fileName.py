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
import os, time
from datetime import datetime, timedelta, date

# fonction pour créer des noms de fichiers avec la date du jours
def fileCreate(prefixe, exten):
    comment_date = date.today() - timedelta(days=0)
    filename = f"{prefixe}-{comment_date}.{exten}"
    return filename

# fonction pour créer des noms de fichiers avec le nombre de jours configurer en rétention (utile pour supprimer les anciens fichiers)
def fileDelete(prefixe, exten, jrs):
    comment_date = date.today() - timedelta(days=jrs)
    filename = f"{prefixe}-{comment_date}.{exten}"
    return filename



