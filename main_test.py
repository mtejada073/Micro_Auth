import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_index_route():
    response = client.get('/authUsers/3')
    assert response.status_code == 200

def test_204():
    response = client.get('/authUsers/99')
    assert response.status_code == 204