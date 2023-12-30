"""
Configuration for test
"""


from typing import Generator
from fastapi.testclient import TestClient
import pytest

from src.gtw.app import app


@pytest.fixture(scope="module")
def test_app() -> Generator[TestClient, None, None]:
    client = TestClient(app)
    yield client
