'''

'''

from ..topics.topic import Topic
from .handler import Handler
from .constants import (
    CONTENT_REF_PREFIX,
    RESET_STATE_PREFIX,
    HANDLER_TYPE_SUBTITLES)


class SubtitlesHandler(Handler):
    def __init__(self) -> None:
        super().__init__(type=HANDLER_TYPE_SUBTITLES)

    def _get_answer_content(self, topic: Topic, hash: str) -> str:
        ''' topic's type specific '''
        topic_data = topic.metadata.content
        if (topic_data.startswith(RESET_STATE_PREFIX)):
            ref = topic_data[len(RESET_STATE_PREFIX):]
            location = f"{topic.metadata.type}/{ref}"
            topic.set_topic_state(f"{location}_state_{hash}", '0')
            return "Ready!"

        if (topic_data.startswith(CONTENT_REF_PREFIX)):
            ref = topic_data[len(CONTENT_REF_PREFIX):]
            location = f"{topic.metadata.type}/{ref}"
            data = topic.get_topic_data_text(location)

            state = topic.get_topic_state(f"{location}_state_{hash}")
            curr_index = int(state if state != '' else '0')
            indexes = topic.get_topic_data_json(f"{location}_index")
            index = indexes[curr_index]

            if curr_index < len(indexes) - 1:
                topic.set_topic_state(
                    f"{location}_state_{hash}",
                    str(curr_index + 1))
            data_list = data.split('\n')
            chank = data_list[index.get('start', 0): index.get('end', 0)]
            topic_data = '\n'.join(chank)
        return topic_data
