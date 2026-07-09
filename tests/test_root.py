from conftest import client

def test_root_endpoint():
    response = client.get("/")

    assert response.status_code == 200
    assert "message" in response.json()