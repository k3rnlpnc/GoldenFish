import pytest
from backend.app import client
from backend.models.Dream import Dream


def test_get_dreams():
    res = client.get('/mywishes/1')

    assert res.status_code == 200
    assert len(res.get_json()) == len(Dream.query.filter_by(owner_id=1).all())
    assert res.get_json()[0]['id'] == 1


def test_put_dream():
    dream = {
        'name': 'Путешествие на Марс',
        'owner_id': 1
    }
    res = client.post('/mywishes/1', json=dream)

    assert res.status_code == 200


def test_update_dream():
    update = {'description': 'Бизнес классом'}
    res = client.put('/mywishes/1/3', json=update)

    assert res.status_code == 200
    assert Dream.query.get(3).description == update['description']


def test_delete_dream():
    res = client.delete('/mywishes/1/3')

    assert res.status_code == 204
    assert Dream.query.get(3) is None