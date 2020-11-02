import time
from watchdog.observers import Observer
from env import TRACKED_FOLDERS
from mFileSystemEventHandler import mHandler
from helpers import mPrint
import sort as sort
import os

observer = Observer()

def setup():
    global observer

    eventHandler = mHandler()

    for folder in TRACKED_FOLDERS:
        mPrint(folder)
        sortExistingFiles(folder)
        setupFolderTrack(folder, eventHandler)
        
    observer.start()

def sortExistingFiles(folder):
    for filename in os.listdir(folder):
        filepath = folder + os.path.sep + filename
        sort.sort(filepath)


def setupFolderTrack(folder, eventHandler):
    observer.schedule(eventHandler, folder, recursive=False)


setup()

try:
    while True:
        time.sleep(3600)
except:
    observer.stop()
observer.join()