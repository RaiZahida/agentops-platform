from conftest import client

def test_root_endpoint():
    response = client.get("/")

    assert response.status_code == 200

    data = response.json()

    assert "application" in data
    assert "version" in data
    assert "status" in data