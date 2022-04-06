#!/usr/bin/python3
import os, time, datetime
from datetime import datetime, timedelta, date



def fileCreate(prefixe, exten):
    comment_date = date.today() - timedelta(days=0)
    print(comment_date)
    filename = f"{prefixe}-{comment_date}.{exten}"
    return filename

def fileDelete(prefixe, exten):
    comment_date = date.today() - timedelta(days=5)
    print(comment_date)
    filename = f"{prefixe}-{comment_date}.{exten}"
    return filename



