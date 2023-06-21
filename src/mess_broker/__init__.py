"""
Message broker pakage
"""

__all__ = ['dsp', 'ProcessingData']


from ..proc_data.schemas.processingdata import ProcessingData
from .mess_dispatcher.mess_dispatcher import MessDispatcher


dsp = MessDispatcher()
