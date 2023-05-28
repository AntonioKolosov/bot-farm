'''

'''


from src.handlers.handler import Handler


class InternalHandler(Handler):
    def __init__(self) -> None:
        super().__init__('internal', ['/help', '/test'])
        self.content = {
            '/help': '''It is a Bot farm.''',
            '/test': 'The bot will send echo messages.'
        }
