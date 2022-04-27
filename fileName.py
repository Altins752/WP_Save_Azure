#!/usr/bin/python3
import os, time
from datetime import datetime, timedelta, date

# fonction pour créer des noms de fichiers avec la date du jours
def fileCreate(prefixe, exten):
    comment_date = date.today() - timedelta(days=0)
    filename = f"{prefixe}-{comment_date}.{exten}"
    return filename

# fonction pour créer des noms de fichiers avec la date d'il y a 5 jours
def fileDelete(prefixe, exten, jrs):
    comment_date = date.today() - timedelta(days=jrs)
    filename = f"{prefixe}-{comment_date}.{exten}"
    return filename



