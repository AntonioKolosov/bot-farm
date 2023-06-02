"""

"""

__all__ = ['dispatch']

from .mess_dispatcher import MessDispatcher

dsp = MessDispatcher()
dispatch = dsp.dispatch_message
