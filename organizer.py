import shutil
import os

from extensions import Extensions
class Organizer(Extensions):
    def __init__(self, dir_path: str):
        self.dir_path: str = dir_path
        self.dir_paths: dict[str, str] = {
            "image": dir_path + "\\Images",
            "video": dir_path + "\\Videos",
            "document": dir_path + "\\Documents",
            "software": dir_path + "\\Softwares",
            "iso": dir_path + "\\ISOs",
            "archived": dir_path + "\\Archives",
            "torrent": dir_path + "\\Torrents",
            "codefiles": dir_path + "\\Codefiles",
            "audio": dir_path + "\\Audios",
            "datafiles": dir_path + "\\Datafiles",
        }
        self.file_extensions: dict[str, set[str]] = {
            "image": self.image_extensions,
            "video": self.video_extensions,
            "document": self.document_extensions,
            "software": self.software_extensions,
            "iso": self.iso_extensions,
            "archived": self.archived_extensions,
            "torrent": self.torrent_extensions,
            "codefiles": self.codefiles_extensions,
            "datafiles": self.datafiles_extensions,
        }

    
    def move(self, file_name: str):
        ext = file_name.split(".")[-1]
        for key, value in self.file_extensions.items():
            if ext in value:
                shutil.move(self.dir_path + "\\" + file_name, self.dir_paths[key])
                print(f"Moved {file_name} to {self.dir_paths[key]}")
                break
        else:
            print(f"Couldn't find a folder for {ext}")

    def organize(self, dir_path: str = None):
        if not dir_path:
            dir_path = self.dir_path
        for _, value in self.dir_paths.items():
            try:
                os.mkdir(value)
            except FileExistsError:
                pass
        for file in os.listdir(dir_path):
            if os.path.isfile(dir_path + "\\" + file):
                self.move(file)
            if os.path.isdir(dir_path + "\\" + file):
                self.organize(dir_path + "\\" + file)
