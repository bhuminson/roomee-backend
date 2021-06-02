from src.Lib.login import getPassword
from src.Lib.login import getId
from src.Tests.test_data import *


def testGetPassword():
    result = getPassword('slimjim')
    assert result == 'password1'


def testWrongPassword():
    result = getPassword('juicewrld999')
    assert result != 'password3'


def testGetId():
    result = getId('dwigt')
    assert result == 3


def testWrongId():
    result = getId('dayday23')
    assert result != 2


def testLogin():
    testGetPassword()
    testWrongPassword()
    testGetId()
    testWrongId()
