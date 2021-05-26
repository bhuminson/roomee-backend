from src.Lib.users import getNextMatchingRoomee
from src.Tests.test_data import *


def testFilters():
    result = getNextMatchingRoomee(7, filter1)
    assert result['username'] == user2['username']
