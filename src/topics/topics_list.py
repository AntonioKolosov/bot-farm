"""
Topics List
"""

from . import Topic
from .loaders import loader


class TopicsList:
    """"
    """
    def __init__(self) -> None:
        self.__topics_list: list[Topic] = []
        self.__init_topics_list()

    @property
    def topics_list(self) -> list[Topic]:
        return self.__topics_list

    def __init_topics_list(self) -> None:
        ''''''
        names = loader.load_names()
        for name in names:
            topic = Topic(name)
            self.__topics_list.append(topic)

    def get_topic(self, name: str, type: str, alias: str) -> Topic:
        ''''''
        for topic in self.__topics_list:
            if (topic.name == name
                    and topic.metadata.service_type == type
                    and topic.metadata.service_alias == alias):
                return topic
        return Topic()

    def get_topic_data_text(self, location: str) -> str:
        """"""
        return loader.load_data_text(location)

    def get_topic_data_json(self, location: str) -> list[dict]:
        """"""
        return loader.load_data_json(location)

    def breaf_topics(self) -> list[dict[str, str]]:
        """"""
        return [{"name": topic.name,
                "descr": topic.metadata.description,
                 "service_type": topic.metadata.service_type,
                 "service_alias": topic.metadata.service_alias}
                for topic in self.topics_list]
