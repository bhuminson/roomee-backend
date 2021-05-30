import pytest
from src.Lib.login import getPassword
from src.Lib.login import getId
from src.Tests.test_data import *

def testGetPassword():
    result = getPassword('dayday23')
    assert result == 'dayday23'

def testWrongPassword():
    result = getPassword('dayday23')
    assert result != 'curry30'

def testGetId():
    result = getId('dayday23')
    assert result == 1

def testWrongId():
    result = getId('dayday23')
    assert result != 2

if __name__ == "__main__":
    testGetPassword()
    testWrongPassword()
    testGetId()
    testWrongId()