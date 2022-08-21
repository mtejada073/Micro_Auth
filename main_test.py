import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_index_route():
    response = client.get('/authUsers/KpNt1iD9AcLtmym')
    assert response.status_code == 200