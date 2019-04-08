import pytest
from app import app

@pytest.fixture
def client():
    return app.test_client()

def test_item_score_works_with_known_pk(client):
    """item_score returns correct score with known pk"""
    expected = b'{"pk": "123", "score": "100"}'
    rv = client.get('/get/123')
    actual = rv.data
    assert expected in actual

def test_item_score_works_with_unknown_pk(client):
    """item_score returns 'score x not found' with unknown pk"""
    expected = b'pk 9999 not found'
    rv = client.get('/get/9999')
    actual = rv.data
    assert expected in actual

def test_item_update_works(client):
    """
    item_update should return 'pk x updated' and
    actually update the data dictionary
    """
    expected_message = b'pk 50 updated with score 90'
    rv_update = client.post('/update', data='{"pk":"50", "score":"90"}', content_type='application/json')
    actual_message = rv_update.data

    rv_get = client.get('/get/50')
    expected_data = b'{"pk": "50", "score": "90"}'
    actual_data = rv_get.data

    assert expected_message in actual_message
    assert expected_data in actual_data
