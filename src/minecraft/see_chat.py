import os
import time


def follow(theFile, ):
    theFile.seek(0, 2)
    while True:
        line = theFile.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line


def seeChat(function, path=os.getenv("APPDATA") + "/.minecraft/logs/latest.log"):
    # encoding = 'utf-8'
    # encoding = 'ISO-8859-1'
    encoding = 'cp1251'
    # encoding = 'ascii'
    logFile = open(path, "r", encoding=encoding)
    logLines = follow(logFile)
    for line in logLines:
        if "]: [CHAT]" in line:
            print(line)
            function(text=line)
