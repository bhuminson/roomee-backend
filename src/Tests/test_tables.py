from src.Lib.users import *
from src.Lib.filters import createNewUserFilters
from src.Tests.test_data import *
from src.constants import testing
from init import app


def insertTestData():
    for user in users:
        createNewUser(user)
    for data in userData:
        createNewUserFilters(data)


def resetTestTables():
    if not testing:
        print("You are not in testing mode.")
        return
    deleteAllUsers()


if __name__ == "__main__":
    with app.app_context():
        resetTestTables()
        insertTestData()
