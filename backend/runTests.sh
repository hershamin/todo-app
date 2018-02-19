#!/bin/sh

echo "\n\n"
echo "========== DJANGO UNIT TESTS =============================="
echo "\n"
export DJANGO_HOST="test"
python todo/manage.py test todo/api/

echo "\n\n"
echo "========== DJANGO REST TESTS =============================="
echo "\n"
#py.test
tavern-ci --stdout todo/test_api.tavern.yaml

