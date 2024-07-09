"""
Base Topics loaders class
"""


from abc import abstractmethod


class Loader:
    def __init__(self, type: str) -> None:
        self.__type = type

    @property
    def type(self) -> str:
        return self.__type

    @abstractmethod
    def load_names(self) -> list[str]:
        """Load all avaible files"""

    @abstractmethod
    def load_metadata(self, name: str) -> dict:
        """Load metadata"""

    @abstractmethod
    def load_content(self, type: str, ref: str) -> dict | str:
        """Load content"""

    @abstractmethod
    def load_state(self, type: str, ref: str) -> str:
        """Load state"""

    @abstractmethod
    def save_state(self, type: str, ref: str, state: str) -> None:
        """Save state"""

    @abstractmethod
    def load_webview(self, app: str, ref: str, page: str) -> dict | str:
        """Load webview"""

    @abstractmethod
    def load_style(self, type: str, ref: str) -> dict | str:
        """Load webstyle"""

    @abstractmethod
    def load_script(self, type: str, ref: str) -> dict | str:
        """Load webscript"""
