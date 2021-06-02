from src.Lib.users import *
from src.Lib.filters import *
from src.Lib.login import *
from src.Tests.test_data import *
from src.constants import testing
from init import app


def insertTestData():
    for user in users:
        createNewUser(user)
    for data in userData:
        createNewUserFilters(data)
    for login in logins:
        createNewLogin(login)


def resetTestTables():
    if not testing:
        print("You are not in testing mode.")
        return
    deleteAllFilters()
    deleteAllUsers()
    deleteAllLogins()


def testSetup():
    with app.app_context():
        resetTestTables()
        insertTestData()
