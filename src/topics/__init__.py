"""
Topics package
"""

__all__ = ["tplst", "Topic"]

from .schemas.topic import Topic
from .topics_list import TopicsList

tplst = TopicsList()
