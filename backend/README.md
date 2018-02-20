# Backend
This will serve as the backend built using the *Django* framework. It will be responsible for hosting the *REST API* endpoints so that the *webapp* and the *android app* can interact with the ToDo list. Additionaly, for simplicty, it will be using a *sqlite* database.

## Requirements
* **Python 2.7:** [Download Link](https://www.python.org/downloads/)
* **Pip:** package manager for python [Download Link](https://pip.pypa.io/en/stable/installing/)
* **Virtual Env:** Isolated environment to safely manage dependencies for python packages [Download Link](https://virtualenv.pypa.io/en/stable/installation/)
* **Virtual Env Wrapper:** Wrapper around *Virtual Environment* [Download Link](https://virtualenvwrapper.readthedocs.io/en/latest/install.html)

## Installation
* Create Virtual Environment: `mkvirtualenv TODO`
* Choose Virtual Environment: `workon TODO`
* Install django `pip install Django` and run `python -m django --version` to confirm [More Information](https://www.djangoproject.com/)
* Install required packages `pip install -r requirements.txt`

## Run Server
* Create migrations for DB `python manage.py makemigrations` from *backend/todo/*
* Apply migrations to DB `python manage.py migrate`
* Run Server `python manage.py runserver 0:8080` to listen on port *8080*
* **NOTE:** Scripts are included for convenience.
* To view database tables, you may create superuser by running `python manage.py createsuperuser`. After that, you can login from [admin](http://localhost:8080/admin).

## Run Tests
* When running tests, in one terminal window, run `runTestPrep.sh` and then run `runTests.sh` in the other window.
* *Option 1*: Run `py.test` from *backend/*
* *Option 2*: Run `tavern-ci --stdout todo/test_api.tavern.yaml`
* **NOTE:** Scripts are included for convenience.