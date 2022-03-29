import time
import os

def CreateFileNametocreate(prefixe, exten):
    fileTime = time.localtime(time.time())

    year = fileTime.tm_year
    month = fileTime.tm_mon
    day = fileTime.tm_mday + 1

    filename = f"{prefixe}_{year}-{month}-{day}.{exten}"
    return filename


def CreateFileNameToDelete(prefixe, exten):
    fileTime = time.localtime(time.time())

    year = fileTime.tm_year
    month = fileTime.tm_mon
    day = fileTime.tm_mday - 4

    filename = f"{prefixe}_{year}-{month}-{day}.{exten}"
    return filename

testCreate = CreateFileNametocreate("test", "txt")
testDelete = CreateFileNameToDelete("test", "txt")

os.system(f"touch {testCreate}")


print(f"Fichier créer : {testCreate}")
print(f"Fichier suprimer : {testDelete}")


os.system(f"azcopy cp '{testCreate}' 'https://bckpwpp6oc.blob.core.windows.net/test/?sp=racwd&st=2022-03-29T12:14:18Z&se=2022-03-29T20:14:18Z&spr=https&sv=2020-08-04&sr=c&sig=RoQzTNGwBbQOriH8E7UiZSOTZCGMhgLzPJRlS1vEXAE%3D'")
os.system(f"azcopy rm 'https://bckpwpp6oc.blob.core.windows.net/test/{testDelete}?sp=racwd&st=2022-03-29T12:14:18Z&se=2022-03-29T20:14:18Z&spr=https&sv=2020-08-04&sr=c&sig=RoQzTNGwBbQOriH8E7UiZSOTZCGMhgLzPJRlS1vEXAE%3D'")

os.system(f"rm {testCreate}")