#!/bin/sh

python todo/manage.py makemigrations
python todo/manage.py migrate
