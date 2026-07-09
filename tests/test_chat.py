from conftest import client
from unittest.mock import patch


@patch("app.routes.chat.llm_service.generate_response")
def test_chat_endpoint(mock_generate_response):
    mock_generate_response.return_value = "Mock response"

    response = client.post(
        "/chat",
        json={
            "message": "Hello"
        }
    )

    assert response.status_code == 200
    assert response.json() == {
        "response": "Mock response"
    }