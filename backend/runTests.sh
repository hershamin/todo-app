#!/bin/sh

echo "\n\n"
echo "========== DJANGO UNIT TESTS =============================="
echo "\n"
export DJANGO_HOST="test"
python todo/manage.py test todo/api/

echo "\n\n"
echo "========== DJANGO REST TESTS (USER) =============================="
echo "\n"
#py.test
tavern-ci --stdout todo/api_tests/test_user.tavern.yaml

echo "\n\n"
echo "========== DJANGO REST TESTS (TASK) =============================="
echo "\n"
tavern-ci --stdout todo/api_tests/test_task.tavern.yaml

rm todo/todo-testDB.sqlite3
