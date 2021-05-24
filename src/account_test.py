from db import executeQuery
import pytest

def test_username():

    result = executeQuery( 'SELECT username \
                            FROM users \
                            WHERE id=%s ', [1]).get('username')
    assert result =='dayday23'


def test_firstname():
    result = executeQuery( 'SELECT firstname \
                            FROM test_users \
                            WHERE id = %s', [100]).get('firstname')
    assert result =='Draymond'


def test_lastname():
    result = executeQuery('SELECT * \
                            FROM test_users \
                            WHERE \
                            id = %s', [100]).get('lastname')
    assert result =='Green'


def test_nickname():
    result = executeQuery('SELECT nickname \
                            FROM test_users \
                            WHERE \
                            id = %s', [100]).get('nickname')
    assert result =='Day day'


def test_phone():
    result = executeQuery('SELECT phone \
                            FROM test_users \
                            WHERE \
                            id = %s', [100]).get('phone')
    assert result =='5105105100'


def test_email():
    result = executeQuery('SELECT email \
                            FROM test_users \
                            WHERE \
                            id =%s',[100]).get('email')
    assert result =='q3@gmail.com'
    

def test_bio():
    result = executeQuery('SELECT bio \
                            FROM test_users \
                            WHERE \
                            id =%s',[100]).get('bio')
    assert result =='pf/c at gsw'
    