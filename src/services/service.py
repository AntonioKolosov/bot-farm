"""
"""


class Service:
    """Base servise"""
    def __init__(self, type: str = "") -> None:
        self._service_type = type

    def __make_endpoints(self) -> None:
        """Instantiate enpoints"""

    async def startup(self, topics_names: list[dict[str, str]]) -> None:
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
