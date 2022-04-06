import os
from fileName import fileCreate

def DumpMysql(username, password):
    filename = fileCreate("wp_bdd_bckp", "sql")
    foldername = "./bckp_wp"
    filename = f"{foldername}/{filename}"
    os.system(f"mysqldump -u {username} -p{password} wp202203_p6OC > {filename}")
    return foldername
