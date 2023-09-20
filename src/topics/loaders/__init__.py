"""
Topics loaders package
"""

__all__ = ['loader']
from .loader_factory import LoaderFactory

LOADER_BASE = "BASE"
LOADER_FS = "FS"


loader = LoaderFactory().loader()
