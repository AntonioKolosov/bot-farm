"""
FS loader
"""

import os
import json
from pathlib import Path
from ..schemas.topic import Topic
from .loader import Loader


class FsLoader(Loader):
    def __init__(self) -> None:
        super().__init__("FS")
        self.__storage = os.environ.get("FS_TOPICS_METADATA_STORAGE",
                                        "./datatopics")
        self.__load_metadata()

    def __load_metadata(self) -> None:
        """"""
        path = Path(self.__storage)
        for file in path.iterdir():
            if file.suffix == '.json':
                ffn = f'{self.__storage}/{file.name}'
                with open(ffn, 'r') as json_file:
                    top_obj = json.load(json_file)
                # Read topic
                topic = Topic(**top_obj)
                super().metadata.append(topic)
