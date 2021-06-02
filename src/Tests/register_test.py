from src.db import executeQuery
from src.Tests.test_data import *


def test_username():

    result = executeQuery('SELECT username \
                            FROM test_users \
                            WHERE id=%s ', [1]).get('username')
    assert result == user1['username']


def test_firstname():
    result = executeQuery('SELECT firstname \
                            FROM test_users \
                            WHERE id = %s', [1]).get('firstname')
    assert result == user1['firstname']


def test_lastname():
    result = executeQuery('SELECT lastname \
                            FROM test_users \
                            WHERE \
                            id = %s', [1]).get('lastname')
    assert result == user1['lastname']


def test_nickname():
    result = executeQuery('SELECT nickname \
                            FROM test_users \
                            WHERE \
                            id = %s', [1]).get('nickname')
    assert result == user1['nickname']


def test_phone():
    result = executeQuery('SELECT phone \
                            FROM test_users \
                            WHERE \
                            id = %s', [1]).get('phone')
    assert result == user1['phone']


def test_email():
    result = executeQuery('SELECT email \
                            FROM test_users \
                            WHERE \
                            id =%s', [1]).get('email')
    assert result == user1['email']


def test_bio():
    result = executeQuery('SELECT bio \
                            FROM test_users \
                            WHERE \
                            id =%s', [1]).get('bio')
    assert result == user1['bio']


def testRegister():
    test_username()
    test_firstname()
    test_lastname()
    test_nickname()
    test_phone()
    test_email()
    test_bio()
