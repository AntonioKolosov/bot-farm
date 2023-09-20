"""
Topics loaders package
"""

__all__ = ['loader']
from .loader_factory import LoaderFactory

loader = LoaderFactory().loader()
