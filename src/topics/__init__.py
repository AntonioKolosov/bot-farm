"""
Topics package
"""

# __all__ = ["tplst", "topics_by_type", "Topic"]
__all__ = ["tplst", "Topic"]

from .schemas.topic import Topic
# from .topics_loader import load_topics_by_type
from .topics_list import TopicsList

# topics_by_type = load_topics_by_type

tplst = TopicsList()
