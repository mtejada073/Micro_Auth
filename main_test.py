import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_index_route():
    response = client.get('/authUsers/50')
    assert response.status_code == 200