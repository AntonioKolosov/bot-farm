'''

'''

from ..topics.topic import Topic
from .handler import Handler
from .constants import HANDLER_TYPE_SUBTITLES


class SubtitlesHandler(Handler):
    def __init__(self) -> None:
        super().__init__(type=HANDLER_TYPE_SUBTITLES)

    def _get_answer_content(self, topic: Topic, ref: str, hash: str) -> str:
        ''' topic's type specific '''
        location = f"{topic.metadata.type}/{ref}"
        data = topic.get_topic_data_text(location)
        data_list = data.split('\n')
        state = topic.get_topic_state(f"{location}_{hash}")
        curr_index = int(state if state != '' else '0')
        indexes = topic.get_topic_data_json(f"{location}_index")
        index = indexes[curr_index]
        if curr_index < len(indexes) - 1:
            topic.set_topic_state(f"{location}_{hash}", str(curr_index + 1))
        chank = data_list[index.get('start', 0): index.get('end', 0)]
        return '\n'.join(chank)
