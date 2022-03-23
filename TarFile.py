import tarfile
import os
from fileName import CreateFileName


def creatArchive(foldername):
    archivename = CreateFileName("bckp_wp","tar.gz")
    backup = tarfile.open(archivename, mode='w:gz')
    backup.add(foldername)
    backup.close()
    os.system("rm -rf bckp_wp")
    return archivename