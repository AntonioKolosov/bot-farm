"""
Test message from TG
"""


import pytest
from src.mess_broker import dsp


test_message_from_tg = {
    "update_id": 773055060,
    "message": {
        "message_id": 16,
        "from": {
            "id": 123456789,
            "is_bot": False,
            "first_name": "John",
            "username": "John",
            "language_code": "ru",
            "is_premium": True
        },
        "chat": {
            "id": 123456789,
            "first_name": "John",
            "username": "slam_damage",
            "type": "private"
        },
        "date": 1678112773,
        "text": "Hello!"
    }
}


test_response_message = {"result": "Message sent to the dispatcher"}


@pytest.mark.hook
@pytest.mark.parametrize("data, expected_value",
                         [(test_message_from_tg, test_response_message)])
def test_message(test_app, monkeypatch, data, expected_value):
    """Test without real call post message"""
    async def mock_dispatch_message(self_ref):
        return True

    monkeypatch.setattr(dsp, "dispatch_message", mock_dispatch_message)
    response = test_app.post("/tgincdata/0", json=data)
    assert response.status_code == 200
    assert response.json() == expected_value
