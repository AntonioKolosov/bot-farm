"""
Topics List
"""

import os
from .schemas.topic import Topic
from .loaders.loader import Loader
from .loaders.fsloader import FsLoader


class TopicsList:
    """"
    """
    def __init__(self) -> None:
        loader_type = os.environ.get("TOPICS_METADATA_LOADER_TYPE", "FS")
        self.__loader: Loader = self.__loaders_factory(loader_type)
        self.__topics_metadata: list[Topic] = self.__loader.metadata

    @property
    def topics_metadata(self) -> list[Topic]:
        return self.__topics_metadata

    def topics_by_type(self, type: str) -> list[Topic]:
        """"""
        return [topic for topic in self.topics_metadata if topic.type == type]

    def topics_by_service_id(self, service_id: str) -> list[Topic]:
        """"""
        return [topic for topic in self.topics_metadata
                if topic.service_id == service_id]

    def topics_name_by_service_id(self, service_id: str) -> list[str]:
        """"""
        return [topic.name for topic in self.topics_by_service_id(service_id)]

    def breaf_topics(self) -> list[dict[str, str]]:
        """"""
        return [{"name": topic.name,
                "descr": topic.description,
                 "service_type": topic.service_type,
                 "service_id": topic.service_id}
                for topic in self.topics_metadata]

    def get_content(self, topic: Topic) -> str:
        """"""
        return self.__loader.load_content(topic.content)

    def __loaders_factory(self, type: str) -> Loader:
        """"""
        if type == "FS":
            return FsLoader()
        return Loader("BASE")
