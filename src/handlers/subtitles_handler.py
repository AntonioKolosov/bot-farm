'''

'''

from src.handlers.handler import Handler


class SubtitlesHandler(Handler):
    def __init__(self) -> None:
        super().__init__(type="subtitles")
        self._load_topics()
