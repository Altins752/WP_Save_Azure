import time
import os

def CreateFileName(prefixe, exten):
    fileTime = time.localtime(time.time())

    year = fileTime.tm_year
    month = fileTime.tm_mon
    day = fileTime.tm_mday

    filename = f"{prefixe}_{year}-{month}-{day}.{exten}"
    return filename