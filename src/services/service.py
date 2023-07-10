"""
"""


from src.proc_data.schemas.answeringdata import AnsweringData


class Service:
    """Base servise"""
    def __init__(self, type: str = "") -> None:
        self._service_type = type
        self._breaf_topics: list[dict[str, str]] = []
        self._bots_id_2_names: list = []

    def __make_endpoints(self) -> None:
        """Instantiate enpoints"""

    def get_alias(self, service_id: str) -> str:
        """"""
        for id_2_name in self._bots_id_2_names:
            id, name = id_2_name.split(":")
            if id == service_id:
                return name
        return "default"

    def add_breaf(self, topic: dict[str, str]) -> None:
        """"""
        self._breaf_topics.append(topic)

    async def startup(self) -> None:
        """"""

    async def shutdown(self) -> None:
        """"""

    def __endpoint_for_request(self,
                               bot_id: str,
                               method: str,
                               params: dict | None = None) -> str:
        return "base service endpoint"

    async def send_message(self, answer: AnsweringData) -> bool:
        """"""
        return True
