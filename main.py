import time
import sys

from handler import Handler
from organizer import Organizer
from watchdog.observers import Observer

def main():
    if sys.argv[1:]:
        downloads_path = sys.argv[1]
    else:
        print("Please provide a path to the downloads folder")
        print("Usage: python main.py <path>")
        exit(1)

    downloads_path = sys
    organizer = Organizer(downloads_path)
    handler = Handler(organizer)
    observer = Observer()

    observer.schedule(handler, path=downloads_path, recursive=True)

    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        observer.join()

if __name__ == "__main__":
    main()

