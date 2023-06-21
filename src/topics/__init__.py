"""
Topics package
"""

__all__ = ["topics_by_type", "Topic"]

from .schemas.topic import Topic
from .topics_loader import load_topics_by_type

topics_by_type = load_topics_by_type
