import pytest
import os
import requests
from api.client import Client

@pytest.fixture
def client():
    return Client()

@pytest.mark.skip(reason='Needs server online for testing.')
def test_get_score_works_with_pk(client):
    """Works with known existing pk"""
    score = client.get_score(123)
    assert score == 100

@pytest.mark.skip(reason='Needs server online for testing.')
def test_get_score_works_with_no_pk(client):
    """Returns None and message if pk doesn't exist"""
    score = client.get_score(9999)
    assert score is None

@pytest.mark.skip(reason='Needs server online for testing.')
def test_get_score_works_with_none(client):
    """Returns message saying that there is no such pk"""
    score = client.get_score(None)
    assert score is None

@pytest.mark.skip(reason='Needs server online for testing.')
def test_update_line_works(client):
    url = client.base_url + '/update'
    result = client._update_line(url, '{"pk":"50", "score":"90"}')
    assert result is None

@pytest.mark.skip(reason='Needs server online for testing.')
def test_update_line_raises_error_for_invalid_request(client):
    url = client.base_url + '/update'
    with pytest.raises(requests.exceptions.HTTPError):
        client._update_line(url, '{"pk":"50"}')

def test_filenames_are_correctly_read(client):
    filenames = ['example' + '/' + s for s in os.listdir('example') if client.json_pattern.match(s)]
    assert filenames == ['example/example_data_1.jsonl', 'example/example_data_2.jsonl']

def test_first_line_in_jsonl_examples_is_correct(client):
    expected = '{ "pk": "123", "score": "100" }'
    actual = client._get_lines('example')[0]
    assert expected == actual

def test_length_jsonl_examples_is_6(client):
    length = len(client._get_lines('example'))
    assert length == 6