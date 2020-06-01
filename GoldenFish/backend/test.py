import pytest
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity
from backend.app import client
from backend.models.Dream import Dream


def test_register():
    data = {
        'name': 'Name',
        'surname': 'Surname',
        'email': 'someemail@mail.com',
        'username': 'Username',
        'password': 'qwerty'
    }
    res = client.post('/registration', json=data)

    assert res.status_code == 200


def test_authenticate():
    data = {
        'email': 'someemail@mail.com',
        'password': 'qwerty'
    }
    res = client.post('/authentication', json=data)
    assert res.status_code == 200


def test_get_dreams():
    headers = {
        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1OTEwMTUyNDgsIm5iZiI6MTU5MTAxNTI0OCwianRpIjoiYjQ1N2VlYjktODkyNS00MmQ1LWIxODAtNDI0NDBmYWIxMmRkIiwiZXhwIjoxNTkzMDg4ODQ4LCJpZGVudGl0eSI6NywiZnJlc2giOmZhbHNlLCJ0eXBlIjoiYWNjZXNzIn0.EXKctq1DY2kqrXwTlBsUAuV775JV9JHu7TVVJMDFEh0'
    }
    res = client.get('/mywishes', headers=headers)
    user_id = get_jwt_identity()

    assert res.status_code == 200
    assert len(res.get_json()) == len(Dream.query.filter_by(owner_id=user_id).all())

'''
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
'''