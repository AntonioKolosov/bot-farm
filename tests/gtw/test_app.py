"""
"""


import pytest


@pytest.mark.root
def test_read_main(test_app):
    response = test_app.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "I am your Bot"}
