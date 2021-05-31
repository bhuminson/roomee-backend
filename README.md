# Roommate Finder Webapp

[![Build Status](https://www.travis-ci.com/bhuminson/roomee-backend.svg?token=EqCjonQA1dTt9y36y2D9&branch=main)](https://www.travis-ci.com/bhuminson/roomee-backend)

This app helps to find roommates.

# Demo

https://roomeeapp.herokuapp.com/#/search

# Features


# Requirement

* python 3.8

# Installation
create a virtual environment
```bash
pip install -r requirements.txt
```

# Usage
This app uses a server on heroku by default.
```bash
git clone https://github.com/bhuminson/roomee-backend.git
cd roomee-backend
export FLASK_APP=init.py
export FLASK_ENV=development
flask run
```
# Local server setup
Install pgadmin4 and create a new server with host, db, user, pw in constants.py.
copy appdb.sql and run it in pgadmin4. This should create new database.

# Development
In constants.py
```bash
dev= True
```

# Testing
In constants.py
```
testing = True
```
then
```bash
cd/src/Tests
pytest filename.py
```


# CI/CD



# Linters


Style-Checking:

For JavaScript, add VSCode extension Prettier

For Python, use VSCode extension Python by Microsoft

In settings, check "Format on Save" to style check on every save.

Use the default settings for both linters.
