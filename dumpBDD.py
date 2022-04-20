#!/usr/bin/python3
import os
from fileName import fileCreate

def DumpMysql(username, password, bddname, foldername):
    filename = fileCreate("wp_bdd_bckp", "sql")
    filename = f"{foldername}/{filename}"
    os.system(f"mysqldump -u {username} -p{password} {bddname} > {filename}")
    return foldername
