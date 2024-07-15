
import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Set the path for the directory to track changes
from_dir = "<Set path for tracking file system events>"

class FileEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(f"Created: {event.src_path}")

    def on_modified(self, event):
        print(f"Modified: {event.src_path}")

    def on_moved(self, event):
        print(f"Moved: from {event.src_path} to {event.dest_path}")

    def on_deleted(self, event):
        print(f"Deleted: {event.src_path}")

if __name__ == "__main__":
    # Initialize event handler
    event_handler = FileEventHandler()

    # Initialize observer
    observer = Observer()
    observer.schedule(event_handler, path=from_dir, recursive=True)

    # Start the observer
    observer.start()
    print(f"Started monitoring {from_dir}")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
    print(f"Stopped monitoring {from_dir}")