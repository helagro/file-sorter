import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
from env import TRACKED_FOLDERS

observer = None

def setup():
    global observer
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
        if(self.isAddEvent(event)):
            self.onAdded(event)

    def isAddEvent(self, event):
        className = event.__class__.__name__
        return className == "FileModifiedEvent" or className == "FileCreatedEvent"

    def onAdded(self, event):
        filename = event.src_path

        extension = os.path.splitext(filename)[1]
        mPrint(filename, extension)


setup()


try:
    while True:
        time.sleep(3600)
except:
    observer.stop()
observer.join()