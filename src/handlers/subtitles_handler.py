'''

'''

from ..topics.topic import Topic
from .handler import Handler
from .constants import HANDLER_TYPE_SUBTITLES


class SubtitlesHandler(Handler):
    def __init__(self) -> None:
        super().__init__(type=HANDLER_TYPE_SUBTITLES)

    def _get_answer_content(self, topic: Topic, ref: str) -> str:
        ''' topic's type specific '''
        location = f"{topic.metadata.type}/{ref}"
        data = topic.get_topic_data_text(location)
        data_list = data.split('\n')
        indexes = topic.get_topic_data_json(f"{location}_index")
        index = indexes[5]
        chank = data_list[index.get('start', 0): index.get('end', 0)]
        return '\n'.join(chank)
