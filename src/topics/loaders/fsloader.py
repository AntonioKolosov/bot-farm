"""
FS loader
"""

import os
import json
from pathlib import Path
from ..schemas.topic import Topic
from .loader import Loader
from . import LOADER_FS


class FsLoader(Loader):
    def __init__(self) -> None:
        super().__init__(LOADER_FS)
        self.__storage = os.environ.get("FS_TOPICS_STORAGE",
                                        "./datatopics_example")
        self.__load_metadata()

    def __load_metadata(self) -> None:
        """"""
        path = Path(self.__storage)
        for file in path.iterdir():
            if file.suffix == '.json':
                top_obj = self.load_data_json(file.stem)
                # Read topic
                topic = Topic(**top_obj)
                super().metadata.append(topic)

    def load_data_text(self, location: str) -> str:
        """"""
        ffn = f"{self.__storage}/{location}.txt"
        with open(ffn, 'r') as f:
            top_content = f.read()
        return top_content

    def load_data_json(self, location) -> dict:
        ''''''
        ffn = f"{self.__storage}/{location}.json"
        with open(ffn, 'r') as json_file:
            return json.load(json_file)
