"""
Message handlers package
"""

__all__ = ["hnd"]


from .active_handlers import ActiveHandlers


hnd = ActiveHandlers()
