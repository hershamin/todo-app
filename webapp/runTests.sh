#!/bin/sh

echo "\n\n"
echo "========== Running KarmaJS tests =============================="
echo "\n"
node_modules/karma-cli/bin/karma start karma.conf.js
echo "\n\n"
echo "========== Running Selenium tests =============================="
echo "\n"
python tests/overall-test.py

