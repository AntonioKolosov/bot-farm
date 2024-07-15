"""
Send message to telegram chats, bots
"""


import json
from src.config import cfg
from src.data_def import utilites
from src.data_def.schemas.answeringdata import AnsweringData
from ..service import Service
from .tgapi import send_message
from .tgapi import set_webhook, delete_webhook, set_description
from .tgapi import delete_commands, set_command, get_commands
from .tgapi import get_chat_menu_button, set_chat_menu_button
from .tgapi import set_keyboard_button


class TgService(Service):
    """Telegram service"""
    def __init__(self) -> None:
        super().__init__("TG")
        self.__endpoint_template = "https://api.telegram.org/bot{key}/{method}"
        self.__tokens = cfg.tokens
        self.__gtw_url = cfg.gtw_url
        self._bots_id_2_names: list[str] = cfg.bots_id_2_names
        self.__endpoints: dict[str, str] = {}
        self.__make_endpoints()

    async def send_message(self, answer: AnsweringData) -> bool:
        """Wrapper for API"""
        bot_id = self._get_id_by_alias(answer.service_alias)
        endpoint = self.__endpoints.get(bot_id, "")
        tg_answer = utilites.tg_answer_converter(bot_id, answer)
        return await send_message(endpoint, tg_answer)

    async def set_buttons(self, answer: AnsweringData) -> bool:
        """Wrapper for API"""

        buttons = self.__create_buttons_data(answer)
        bot_id = self._get_id_by_alias(answer.service_alias)
        endpoint = self.__endpoints.get(bot_id, "")
        return await set_keyboard_button(endpoint, buttons)

    def __create_buttons_data(self, answer: AnsweringData):
        """Create buttons data"""
        service_metadata = self._service_metadata.get(answer.service_alias,
                                                      None)
        if service_metadata is None:
            return

        # Array of Arrays of KeyBoardButton
        keyboard = []
        buttons = {}
        for cmd in service_metadata.commands:
            if cmd.button:
                # KeyboardButton
                if cmd.content.startswith('@webapp---'):
                    # the button will start a web app
                    path = cmd.content[len('@webapp---'):]
                    url = 'data-feed-service.onrender.com'
                    button = [{"text": cmd.name[1:].upper(),
                               "web_app": {"url": f'{url}/{path}'}}]
                else:
                    # the button will perform a regular task
                    button = [{"text": cmd.name}]
                keyboard.append(button)

        # ReplayKeyboardMarkup
        if len(keyboard) > 0:
            keyboard_buttons = {
                "keyboard": keyboard,
                "resize_keyboard": True,
                "one_time_keyboard": False
            }

            keyboard_buttons = json.dumps(keyboard_buttons)

            buttons = {
                "chat_id": int(answer.content),
                "text": "Press a button to continue",
                "reply_markup": keyboard_buttons
            }

        return buttons

    async def startup(self) -> None:
        """Set webhook"""
        for b_id, ep in self.__endpoints.items():
            await self.__initialize(b_id)

    async def shutdown(self) -> None:
        """Unset webhook"""
        for b_id, ep in self.__endpoints.items():
            await self.__close(b_id)

    async def set_description(self, service_id: str, descr: str) -> bool:
        """Set description"""
        return await self.__set_description(service_id, descr)

    async def __initialize(self, bot_id: str) -> None:
        """Initialize webhooks, buttons, menu, commands"""
        # convert bot_id to bot_name
        alias = self._get_alias_by_id(bot_id)
        print(f"Initialize the {alias} endpoint")

        await self.__delete_menu_commands(bot_id)
        await self.__set_menu_commands(bot_id)
        await self.__set_menu_button(bot_id, True)
        await self.__set_webhook(bot_id, alias)

    async def __close(self, bot_id: str) -> None:
        """Close webhooks, buttons, menu, commands"""
        alias = self._get_alias_by_id(bot_id)
        print(f"CLose the {alias} endpoint")
        await self.__delete_webhook(bot_id)
        await self.__delete_menu_commands(bot_id)
        await self.__set_menu_button(bot_id)

    async def __set_webhook(self, bot_id: str, alias: str) -> bool:
        """Wrapper for API"""
        endpoint = self.__endpoints.get(bot_id, "")
        gtw_url = f"{self.__gtw_url}/tgincdata/{alias}"
        return await set_webhook(endpoint, gtw_url)

    async def __delete_webhook(self, bot_id: str) -> bool:
        """Wrapper for API"""
        endpoint = self.__endpoints.get(bot_id, "")
        return await delete_webhook(endpoint)

    async def __delete_menu_commands(self, bot_id) -> bool:
        """Wrapper for API"""
        endpoint = self.__endpoints.get(bot_id, "")
        return await delete_commands(endpoint)

    async def __get_menu_commands(self, bot_id) -> bool:
        """Wrapper for API"""
        endpoint = self.__endpoints.get(bot_id, "")
        return await get_commands(endpoint)

    async def __set_description(self, service_id: str, descr: str) -> bool:
        """Wrapper for API"""
        endpoint = self.__endpoints.get(service_id, "")
        return await set_description(endpoint, descr)

    async def __set_menu_commands(self, bot_id: str) -> bool:
        """Wrapper for API"""
        alias = self._get_alias_by_id(bot_id)
        bot_metadata = self._service_metadata.get(alias, None)
        if bot_metadata is None:
            return False
        commands = []
        for command in bot_metadata.commands:
            if command.menu:
                cmd = {
                    "command": command.name,
                    "description": command.description
                }
                commands.append(cmd)
        endpoint = self.__endpoints.get(bot_id, "")
        return await set_command(endpoint, commands)

    async def __set_menu_button(self, bot_id: str, cmd: bool = False) -> bool:
        """Wrapper for API"""
        button = {"type": "default"}
        if cmd:
            button = {"type": "commands"}
        endpoint = self.__endpoints.get(bot_id, "")
        return await set_chat_menu_button(endpoint, button)

    async def __get_menu_button(self, bot_id: str) -> bool:
        """Wrapper for API"""
        endpoint = self.__endpoints.get(bot_id, "")
        return await get_chat_menu_button(endpoint)

    def __make_endpoints(self) -> None:
        """Instantiate enpoints"""
        for t in self.__tokens:
            bot_id, _ = t.split(":")

            endpoint = self.__set_token_to_endpoint(t)
            self.__endpoints[bot_id] = endpoint

    def __set_token_to_endpoint(self, token: str) -> str:
        """Set token for an endpoint"""
        return self.__endpoint_template.format(key=token, method="{method}")
