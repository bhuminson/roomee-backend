from src.Tests.filters_test import testFilters
from src.Tests.test_tables import testSetup
from src.Tests.login_test import testLogin
from src.constants import testing

testing = True

if __name__ == "__main__":
    testSetup()
    testFilters()
    testLogin()