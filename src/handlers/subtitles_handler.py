"""
Special handler for Theatre Project.
"""


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
        """ Topic's type specific """
        content = ''
        if (cmd_data.content.startswith(RESET_STATE)):
            ref = cmd_data.content[len(RESET_STATE):]
            if (RETURN_TO_SENDER in ref):
                ref, content = ref.split(RETURN_TO_SENDER)
            loader.save_state(cmd_data.type, f"{ref}_state_{hash}", '0')
        if (cmd_data.content.startswith(CONTENT_REF)):
            ref = cmd_data.content[len(CONTENT_REF):]
            f"{cmd_data.type}/{ref}"

            state = int(loader.load_state(cmd_data.type,
                                          f"{ref}_state_{hash}"))
            content_dict = loader.load_content(cmd_data.type, ref)
            if type(content_dict) == dict:
                content_list = content_dict['content']
                if state >= len(content_list):
                    state -= 1
                content = content_list[state]['chank']

            loader.save_state(
                cmd_data.type,
                f"{ref}_state_{hash}",
                str(state + 1)
            )

        return content
