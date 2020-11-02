import time
from watchdog.observers import Observer
from env import TRACKED_FOLDERS
from mFileSystemEventHandler import mHandler
from helpers import mPrint

observer = None

def setup():
    global observer
    mPrint("Started")

    observer = Observer()
    eventHandler = mHandler()
    scheduleFolders(observer, eventHandler, 0)

    observer.start()

def scheduleFolders(observer, eventHandler, nextFolderIndex):
    if nextFolderIndex >= len(TRACKED_FOLDERS):
        return

    folder = TRACKED_FOLDERS[nextFolderIndex]
    mPrint(folder)
    observer.schedule(eventHandler, folder, recursive=False)

    nextFolderIndex += 1
    scheduleFolders(observer, eventHandler, nextFolderIndex)



setup()


try:
    while True:
        time.sleep(3600)
except:
    observer.stop()
observer.join()