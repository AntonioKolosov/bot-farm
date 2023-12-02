"""
FS loader - Loads a topic metadata and content from the file system
"""


import json

from ..config import cfg
from pathlib import Path
from .loader import Loader


class FsLoader(Loader):
    def __init__(self, type: str) -> None:
        super().__init__(type)
        self.__storage = cfg.storage

    def load_names(self) -> list[str]:
        """"""
        path = Path(self.__storage)
        names = []
        for file in path.iterdir():
            if file.suffix == '.json':
                names.append(file.stem)
        return names

    def load_metadata(self, name) -> dict:
        """"""
        path = Path(self.__storage)
        file_name = ''
        for file in path.iterdir():
            if file.stem == name and file.suffix == '.json':
                file_name = file.stem
                break
        return self.__load_json(file_name)

    def load_content(self, type: str, ref: str) -> dict | str:
        """"""
        location = f"{type}/{ref}"
        ffn = f"{self.__storage}/{location}"
        if type == 'subtitles':
            return self.__load_json(ffn)
        return self.__load_text(ffn)

    def load_state(self, type: str, ref: str) -> str:
        """"""
        location = f"{type}/{ref}"
        ffn = f"{self.__storage}/{location}.txt"
        try:
            with open(ffn, 'r') as f:
                top_content = f.read()
            return top_content
        except (FileNotFoundError):
            return ''

    def save_state(self, type: str, ref: str, state: str) -> None:
        ''''''
        location = f"{type}/{ref}"
        ffn = f"{self.__storage}/{location}.txt"
        with open(ffn, 'w') as f:
            f.write(state)

    def __load_json(self, location: str) -> dict:
        ''''''
        ffn = f"{self.__storage}/{location}.json"
        with open(ffn, 'r') as json_file:
            return json.load(json_file)

    def __load_text(self, location: str) -> str:
        ''''''
        ffn = f"{self.__storage}/{location}.txt"
        with open(ffn, 'r') as text_file:
            return text_file.read()
