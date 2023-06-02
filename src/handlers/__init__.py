"""
Message handlers package
"""

__all__ = ["topic_handler"]


from .active_handlers import ActiveHandlers


hnd = ActiveHandlers()
topic_handler = hnd.get_handler_by_topic
