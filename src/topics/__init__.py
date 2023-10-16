"""
Topics package
"""

__all__ = ["tplst", "Topic", "loader"]

from .topic import Topic
from .topics_list import TopicsList
from .loaders import loader

tplst = TopicsList()
