
from src.Tests.filters_test import testFilters
from src.Tests.test_tables import testSetup
from src.Tests.login_test import testGetPassword, testWrongPassword, testGetId, testWrongId

if __name__ == "__main__":
    testSetup()
    testFilters()
    testGetPassword()
    testWrongPassword()
    testGetId()
    testWrongId()