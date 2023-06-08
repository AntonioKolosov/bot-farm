"""
Web services pakage.
Includes services by type (TG, WA, e.t.c.) and
a collection of a service endpoints
"""

__all__ = ["services"]

from .services_list import ServicesList

# Create services instance
services = ServicesList()
