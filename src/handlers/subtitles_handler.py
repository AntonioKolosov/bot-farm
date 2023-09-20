'''

'''

from src.handlers.handler import Handler
from src.proc_data.schemas.answeringdata import AnsweringData
from src.topics import tplst, Topic
from src.proc_data.schemas.processingdata import ProcessingData


class SubtitlesHandler(Handler):
    def __init__(self) -> None:
        super().__init__(type="subtitles")
        self._load_handler_topics()

    def _create_answer(self,
                       data: ProcessingData,
                       receiver: int | str,
                       topic: Topic) -> AnsweringData:
        """Create answer from topic"""
        content = topic.content
        if topic != self._default_topic:
            content = self.__get_current_chunck(topic)
        return AnsweringData(
            service_type=data.service_type,
            service_alias=data.service_alias,
            receiver_id=receiver,
            content=content)

    def __get_current_chunck(self, topic: Topic) -> str:
        ''''''
        location = f"{topic.type}/{topic.content}"
        data = tplst.get_topic_data_text(location)
        data_list = data.split('\n')
        indexes = tplst.get_topic_data_json(f"{location}_index")
        index = indexes[5]
        chank = data_list[index.get('start', 0): index.get('end', 0)]
        return '\n'.join(chank)