# Flask JWT Auth

[![Build Status](https://travis-ci.org/realpython/flask-jwt-auth.svg?branch=master)](https://travis-ci.org/realpython/flask-jwt-auth)

This is originally taken from the wonderful article from [RealPython](https://realpython.com/token-based-authentication-with-flask)
I don't take any credit for it, just adapted some of the code to more of my likings.

Mostly I switched to Flask CLI instead of Flask-Script.

The project itself showcases how to implement a basic auth system using JWT tokens.

It basically provides a simple server that can:

* Register users
* Login users
* Generate JWT token for registered users
* Get user info assuming a valid JWT token is provided

It's a good way to understand how JWT works, although this example is not taking implementing a real
Oauth dance using JWT tokens, which would be nice but would require more actors in place:

* Resource Server
* Authorization Server
* Client

Maybe a good idea for another test

## Quick Start

### Basics

1. Create and activate a virtual environment
2. Install the requirements

```commandline
pip install -r requirements.txt
``` 

### Set Environment Variables

Update *project/server/config.py*, and then run:

```sh
$ export APP_SETTINGS="project.server.config.DevelopmentConfig"
```

or

```sh
$ export APP_SETTINGS="project.server.config.ProductionConfig"
```

Alternatively, you can use the *.flaskenv* file to set environment variables too

### Create DB

Create the databases in `psql`:

```sh
$ psql
# create database flask_jwt_auth
# create database flask_jwt_auth_testing
# \q
```

Create the tables and run the migrations:

```sh
$ flask create_db
$ flask db init
$ flask db migrate
```

### Run the Application

```sh
$ flask run
```

So access the application at the address [http://localhost:5000/](http://localhost:5000/)


### Testing

Without coverage:

```sh
$ python manage.py test
```

With coverage:

```sh
$ python manage.py cov
```
