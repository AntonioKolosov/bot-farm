"""
"""


class Service:
    """Base servise"""
    def __init__(self, type: str = "") -> None:
        self._service_type = type
        self._breaf_topics: list[dict[str, str]] = []

    def __make_endpoints(self) -> None:
        """Instantiate enpoints"""

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

    async def send_message(self, service_id: str, answer: dict) -> bool:
        """"""
        return True
