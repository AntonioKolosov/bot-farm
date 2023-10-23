"""
Message broker pakage
"""

__all__ = ['dsp']


from .mess_dispatcher.mess_dispatcher import MessDispatcher


dsp = MessDispatcher()
