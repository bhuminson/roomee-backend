from src.db import executeQuery


def createNewUser(username, firstname, lastname, nickname, phone, email):
    return executeQuery('INSERT INTO users (username, firstname, lastname, nickname, phone, email) VALUES (%s, %s, %s, %s, %s, %s)',
                        [username, firstname, lastname, nickname, phone, email], commit=True)
