from src.Tests.filters_test import testFilters
from src.Tests.test_tables import testSetup
from src.Tests.login_test import testLogin
from src.Tests.register_test import testRegister
import src.constants

src.constants.testing = True

if __name__ == "__main__":
    testSetup()
    testFilters()
    testLogin()
    testRegister()
