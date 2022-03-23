import time
import os

def CreateFileName():
    fileTime = time.localtime(time.time())

    year = fileTime.tm_year
    month = fileTime.tm_mon
    day = fileTime.tm_mday
    hour = fileTime.tm_hour
    minute = fileTime.tm_min
    second = fileTime.tm_sec

    filename = f"wp_bckp_{year}-{month}-{day}.sql"
    return filename


def DumpMysql(username, password):
    filename = CreateFileName()
    os.system("mysqldump -u " + username + " -p" + password + " wp202203_p6OC > " + filename)
    return filename

mysqlresult = DumpMysql("admin", "admin")
print(mysqlresult)