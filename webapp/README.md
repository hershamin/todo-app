# Webapp
This will serve as a the web frontend using the *AngularJS* fraework. It will be responsible for serving a simple ToDo app, and will interact with the backend using *REST API*. Additionally it will be using python's built in *SimpleHTTPServer* to serve the files, all of them are static files.

## Requirements
* **Python 2.7:** [Download Link](https://www.python.org/downloads/)
* **Pip:** package manager for python [Download Link](https://pip.pypa.io/en/stable/installing/)
* **Virtual Env:** Isolated environment to safely manage dependencies for python packages [Download Link](https://virtualenv.pypa.io/en/stable/installation/)
* **Virtual Env Wrapper:** Wrapper around *Virtual Environment* [Download Link](https://virtualenvwrapper.readthedocs.io/en/latest/install.html)
* **NodeJS 8.9.4 LTS:** For running unit tests [Download Link](https://nodejs.org/en/)
* **NPM**: For managing NodeJS packages [Download Link](https://www.npmjs.com/get-npm)
* **NodeEnv:** NodeJS virtual environment, will be run inside python virtualenv [Download Link](https://ekalinin.github.io/nodeenv/)

## Instalation
* Create Virtual Environment: `mkvirtualenv TODO`
* Choose Virtual Environment: `workon TODO`
* Install *nodeenv*: `pip install nodeenv==0.6.5`
* Run: `nodeenv -p`

## Run Sever
* Using *SimpleHTTPServer* run `python -m SimpleHTTPServer 8000`, which will serve the site on [http://localhost:8000/](http://localhost:8000).
* **NOTE:** Backend must be running in order to use this site. Scripts are included for convenience purposes.

## Run Tests
* Manually, you can run *karma* unit tests using: `node_modules/karma-cli/bin/karma start karma.conf.js` from the *webapp* directory.
* **NOTE:** Scripts are included for convenience purposes