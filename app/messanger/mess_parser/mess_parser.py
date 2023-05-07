"""
"""


class MessParser:
    def __init__(self) -> None:
        pass

    def pars_incoming_message(self, data):
        """Message parsing"""
        # Messanger(Bot) type
        # Message type(message, edited, forwarded etc.)
        # Chat ID
        chat_id = data["message"]["chat"]["id"]
        text = data["message"]["text"]
        return chat_id, text
