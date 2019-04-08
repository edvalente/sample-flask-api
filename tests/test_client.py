import pytest
from api.client import Client

@pytest.fixture
def client():
    return Client()

def test_get_score_works_with_pk(client):
    """Works with known existing pk"""
    score = client.get_score(123)
    assert score == 100

def test_get_score_works_with_no_pk(client):
    """Returns None and message if pk doesn't exist"""
    score = client.get_score(9999)
    assert score is None

def test_get_score_works_with_none(client):
    """Returns message saying that there is no such pk"""
    score = client.get_score(None)
    assert score is None

