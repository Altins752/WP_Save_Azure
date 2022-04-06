import tarfile
import os
from fileName import fileCreate


def creatArchive(foldername):
    archivename = fileCreate("bckp_wp","tar.gz")
    backup = tarfile.open(archivename, mode='w:gz')
    backup.add(foldername)
    backup.close()
    os.system("rm -rf bckp_wp")
    return archivename