#!/usr/bin/python3
import os, time
from datetime import datetime, timedelta, date

def fileCreate(prefixe, exten):
    comment_date = date.today() - timedelta(days=0)
    filename = f"{prefixe}-{comment_date}.{exten}"
    return filename

def fileDelete(prefixe, exten):
    comment_date = date.today() - timedelta(days=5)
    filename = f"{prefixe}-{comment_date}.{exten}"
    return filename



