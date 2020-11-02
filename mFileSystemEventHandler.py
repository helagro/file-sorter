from watchdog.events import FileSystemEventHandler
from helpers import mPrint
import sort as sort

class mHandler(FileSystemEventHandler):
    def dispatch(self, event):
        if(self.isAddEvent(event)):
            self.onAdded(event)

    def isAddEvent(self, event):
        className = event.__class__.__name__
        return className == "FileModifiedEvent" or className == "FileCreatedEvent"

    def onAdded(self, event):
        filepath = event.src_path
        sort.sort(filepath)