from db import executeQuery
import pytest

def insertTestData():
    executeQuery("INSERT INTO test_users VALUES  (1, Bhumin) ")
    executeQuery("INSERT ... INTO test_users")
    executeQuery("INSERT ... INTO test_users")
    executeQuery("INSERT ... INTO test_users")
    executeQuery("INSERT (1, no pets) INTO test_filters")
    executeQuery("INSERT ... INTO test_filters")
    executeQuery("INSERT ... INTO test_filters")
    executeQuery("INSERT ... INTO test_filters")

def test1():
    result = executeQuery('SELECT * \
                            FROM test_users u \
                            JOIN test_filters AS f ON u.id=f.userId \
                            WHERE \
                            pets = "no pets')
    assertEquals(result, {'1', 'Bhumin'})