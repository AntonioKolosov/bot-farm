"""
Message broker pakage
"""

__all__ = ['dsp', 'ProcessingData']


from .schemas.processingdata import ProcessingData
from .mess_dispatcher.mess_dispatcher import MessDispatcher


dsp = MessDispatcher()
