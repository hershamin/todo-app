#!/bin/sh

export DJANGO_HOST="test"
python todo/manage.py makemigrations
python todo/manage.py migrate
python todo/manage.py runserver 0.0.0.0:8080
