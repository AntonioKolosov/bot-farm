'''
'''

from .loaders import loader
from .schemas.topic_metadata import TopicMetaData


class Topic:
    def __init__(self, name: str = 'default') -> None:
        self.__name: str = f'/{name}'
        if name != 'default':
            self.init_topic_metadata(name)
        else:
            self.__metadata = TopicMetaData()

    @property
    def name(self) -> str:
        return self.__name

    @property
    def metadata(self) -> TopicMetaData:
        return self.__metadata

    def init_topic_metadata(self, name: str) -> None:
        ''''''
        meta_obj = loader.load_metadata(name)
        self.__metadata = TopicMetaData(**meta_obj)  # type: ignore

    def get_topic_data_text(self, location: str) -> str:
        """"""
        return loader.load_data_text(location)

    def get_topic_data_json(self, location: str) -> dict:
        """"""
        return loader.load_data_json(location)

    def get_topic_state(self, location: str) -> str:
        ''''''
        return loader.load_data_text(location)

    def set_topic_state(self, location: str, state: str) -> None:
        ''''''
        loader.save_data_text(location, state)
