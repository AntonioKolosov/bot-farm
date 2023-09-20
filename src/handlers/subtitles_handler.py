'''

'''

from src.topics import tplst
from .handler import Handler
from .constants import HANDLER_TYPE_SUBTITLES


class SubtitlesHandler(Handler):
    def __init__(self) -> None:
        super().__init__(type=HANDLER_TYPE_SUBTITLES)
        self._load_handler_topics()

    def _get_answer_content(self, type: str, ref: str) -> str:
        ''' topic's type specific '''
        location = f"{type}/{ref}"
        data = tplst.get_topic_data_text(location)
        data_list = data.split('\n')
        indexes = tplst.get_topic_data_json(f"{location}_index")
        index = indexes[5]
        chank = data_list[index.get('start', 0): index.get('end', 0)]
        return '\n'.join(chank)
