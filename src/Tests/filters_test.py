import pytest
from src.Lib.users import createNewUser, getNextMatchingRoomee
from src.Lib.filters import createNewUserFilters
from src.Tests.test_data import *


def testFilters():
    result = getNextMatchingRoomee(1, filter1)
    assert result == user2


if __name__ == "__main__":
    testFilters()
