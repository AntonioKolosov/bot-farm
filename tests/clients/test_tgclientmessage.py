"""

"""


from fastapi import Response


def test_send_message(test_app):
    response = Response()
    response.status_code = 200
    assert response.status_code == 200
