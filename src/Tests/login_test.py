import pytest
from src.Lib.login import getPassword
from src.Tests.test_data import *

def testGetPassword():
    result = getPassword('dayday23')
    assert result == 'dayday23'

if __name__ == "__main__":
    testGetPassword()