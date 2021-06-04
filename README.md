# Roommate Finder Webapp

[![Build Status](https://www.travis-ci.com/bhuminson/roomee-backend.svg?token=EqCjonQA1dTt9y36y2D9&branch=main)](https://www.travis-ci.com/bhuminson/roomee-backend)

A roommate finder app geared towards college students.

## Check out the deployed app here:
https://roomeeapp.herokuapp.com

## Requirements
* node 14
* python 3.8

## Installation
```bash
npm install
pip install -r requirements
```

## Local Development
First, clone both repositories
```bash
git clone https://github.com/bhuminson/roommate-finder.git
git clone https://github.com/bhuminson/roomee-backend.git
```
This app uses a server on heroku by default. To connect to a local server, you must install PostgreSQL 13+ and pgAdmin 4. Then, create a new database with the credentials in `constants.py` for `dev=True`.

In `src/constants.py` and `src.constants/.js`, change the following variable to:
```bash
dev= true
```
IMPORTANT: This constant needs to remain as `false` in main, or else the app will break.  

Now, the frontend will connect to your locally running backend, and your backend will connect to your locally hosted database.

To run the frontend, 
```
npm start
```
To run the backend, create a virtual environment using these instructions specific to your OS: https://flask.palletsprojects.com/en/2.0.x/installation/.
In your virtual environment, set the flask variables and run flask.

For Windows:
```
set FLASK_APP=init.py
set FLASK_ENV=development
flask run
```


## Code Style and Linters
Style-Checking:

For JavaScript, add VSCode extension Prettier

For Python, use VSCode extension Python by Microsoft

In settings, check "Format on Save" to style check on every save.

Use the default settings for both linters.

## Testing
Frontend:
`npx cypress run`

Backend:
`pytest test.py`

Pytest coverage report:

![image](https://user-images.githubusercontent.com/24502905/120859685-6c8e3980-c539-11eb-8b64-c49bf7e8cf26.png)
