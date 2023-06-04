"""
Message handlers package
"""

__all__ = ["topic_handler", "topics_names"]


from .active_handlers import ActiveHandlers


hnd = ActiveHandlers()
topic_handler = hnd.get_handler_by_topic
topics_names = hnd.get_topics_names
