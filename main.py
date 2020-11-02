import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
from env import TRACKED_FOLDERS

def setup():
    mPrint("Started")

    observer = Observer()
    eventHandler = mFileSystemEventHandler()
    scheduleFolders(observer, eventHandler, 0)
    observer.start()
    

def mPrint(*str):
    print(str)

def scheduleFolders(observer, eventHandler, nextFolderIndex):
    if(nextFolderIndex >= len(TRACKED_FOLDERS)):
        return

    folder = TRACKED_FOLDERS[nextFolderIndex]
    mPrint(folder)
    observer.schedule(eventHandler, folder, recursive=True)

    nextFolderIndex += 1
    scheduleFolders(observer, eventHandler, nextFolderIndex)


class mFileSystemEventHandler(FileSystemEventHandler):
    def dispatch(self, event):
        if(event.__class__.__name__ == "DirModifiedEvent"):
            self.onModified(event)

    def onModified(self, event):
        mPrint("Modified", event.src_path)


setup()

while True:
    time.sleep(3)