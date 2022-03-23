import os
from dumpBDD import DumpMysql
from TarFile import creatArchive

os.system("mkdir bckp_wp")
os.system("cp -rf /var/www/html/ ./bckp_wp")
os.system("mv ./bckp_wp/html ./bckp_wp/siteWP")

bckpFolder = DumpMysql("admin", "admin")
archiveName = creatArchive(bckpFolder)
print(archiveName)