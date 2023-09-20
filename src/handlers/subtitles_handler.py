'''

'''

from src.proc_data.schemas.answeringdata import AnsweringData
from src.topics import tplst, Topic
from src.proc_data.schemas.processingdata import ProcessingData
from .handler import Handler, REF_PREFIX


class SubtitlesHandler(Handler):
    def __init__(self) -> None:
        super().__init__(type="subtitles")
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
