'''

'''
from ..data_def.schemas.service_md import CommandMetadata
from src.loaders import loader
from .handler import Handler
from .constants import (
    CONTENT_REF,
    RESET_STATE,
    RETURN_TO_SENDER,
    HANDLER_TYPE_SUBTITLES)


class SubtitlesHandler(Handler):
    def __init__(self) -> None:
        super().__init__(type=HANDLER_TYPE_SUBTITLES)

    def _get_answer_content(self, cmd_data: CommandMetadata, hash: str) -> str:
        ''' topic's type specific '''
        content = ''
        if (cmd_data.content.startswith(RESET_STATE)):
            ref = cmd_data.content[len(RESET_STATE):]
            if (RETURN_TO_SENDER in ref):
                ref, content = ref.split(RETURN_TO_SENDER)
            loader.save_state(cmd_data.type, f"{ref}_state_{hash}", '0')

        if (cmd_data.content.startswith(CONTENT_REF)):
            ref = cmd_data.content[len(CONTENT_REF):]
            f"{cmd_data.type}/{ref}"

            state = loader.load_state(cmd_data.type, f"{ref}_state_{hash}")
            curr_index = int(state if state != '' else '0')
            indexes = loader.load_index(cmd_data.type, f"{ref}_index")
            index_descr = indexes[curr_index]
            if curr_index < len(indexes) - 1:
                loader.save_state(
                    cmd_data.type,
                    f"{ref}_state_{hash}",
                    str(curr_index + 1))

            data = loader.load_content(cmd_data.type, ref)
            data_list = data.split('\n')
            chank = data_list[index_descr.get('start', 0):
                              index_descr.get('end', 0)]
            content = '\n'.join(chank)
        return content
