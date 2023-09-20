"""
Topics List
"""

from .schemas.topic import Topic
from .loaders import loader


class TopicsList:
    """"
    """
    def __init__(self) -> None:
        self.__topics_metadata: list[Topic] = loader.metadata

    @property
    def topics_metadata(self) -> list[Topic]:
        return self.__topics_metadata

    def topics_by_type(self, type: str) -> list[Topic]:
        """"""
        return [topic for topic in self.topics_metadata if topic.type == type]

    def topics_by_service_alias(self, service_alias: str) -> list[Topic]:
        """"""
        return [topic for topic in self.topics_metadata
                if topic.service_alias == service_alias]

    def topics_name_by_service_alias(self, service_alias: str) -> list[str]:
        """"""
        return [
            topic.name for topic in self.topics_by_service_alias(service_alias)
            ]

    def breaf_topics(self) -> list[dict[str, str]]:
        """"""
        return [{"name": topic.name,
                "descr": topic.description,
                 "service_type": topic.service_type,
                 "service_alias": topic.service_alias}
                for topic in self.topics_metadata]

    def get_topic_data_text(self, location: str) -> str:
        """"""
        return loader.load_data_text(location)

    def get_topic_data_json(self, location: str) -> list[dict]:
        """"""
        return loader.load_data_json(location)
