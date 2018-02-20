#!/bin/sh

python todo/manage.py makemigrations api
python todo/manage.py makemigrations
python todo/manage.py migrate
python todo/manage.py runserver 0.0.0.0:8080
