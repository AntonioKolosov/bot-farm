"""
"""


from typing import Generator
from fastapi.testclient import TestClient
import pytest

from app.app import app


@pytest.fixture(scope="module")
def test_app() -> Generator[TestClient, None, None]:
    """"""
    client = TestClient(app)
    yield client
