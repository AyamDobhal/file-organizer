from watchdog.events import *
from typing import Union
from organizer import Organizer

class Handler(FileSystemEventHandler):
    def __init__(self, organizer: Organizer) -> None:
        super().__init__()
        self.organizer = organizer

    def on_moved(self, event: Union[DirMovedEvent, FileMovedEvent]):
        self.organizer.move(event.src_path)

    def on_created(self, event: Union[DirCreatedEvent, FileCreatedEvent]):
        self.organizer.move(event.src_path)

    def on_modified(self, event: Union[DirModifiedEvent, FileModifiedEvent]):
        self.organizer.move(event.src_path)

