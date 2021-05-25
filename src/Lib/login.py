from src.db import executeQuery
from src.constants import testing
from psycopg2 import sql

usersTable = "test_users" if testing else "users"
loginTable = "test_login_info" if testing else "login_info"

@pytest.fixture(scope="function")
def getPassword(username):
    hashed_pw = executeQuery(sql.SQL('SELECT password \
                                FROM users \
                                JOIN login_info on id=login_info.userId \
                                WHERE username=%s').format(sql.Identifier(loginTable)),
                                [username])
    return hashed_pw