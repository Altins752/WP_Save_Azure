#!/usr/bin/python3
import tarfile, shutil
from fileName import fileCreate


def creatArchive(foldername):
    archivename = fileCreate("bckp_wp","tar.gz")
    backup = tarfile.open(archivename, mode='w:gz')
    backup.add(foldername)
    backup.close()
    shutil.rmtree("bckp_wp")
    return archivename