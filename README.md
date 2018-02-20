# ToDo App
The key motivation for building a simple ToDo app here in an open source repository is to demonstrate best practices for coding as well as testing the code. Here, *backend* and *frontend* or *mobile app* will communicate with each other using [REST API](http://www.restapitutorial.com/).

## Technology stack
* [Django](https://www.djangoproject.com/) (*Backend*)
* [AngularJS](https://angularjs.org/) (*Frontend*)
* [Android](https://www.android.com/) (*Mobile App*)

## Testing stack
* Django [test](https://docs.djangoproject.com/en/2.0/topics/testing/overview/) (*unit*)
* AngularJS [test](http://andyshora.com/unit-testing-best-practices-angularjs.html) (*unit* + *UI*)
* [Expresso](https://developer.android.com/training/testing/espresso/index.html) (*Android UI*)
* [Roboelectric](http://robolectric.org/) (*Android unit*)
* [Tavern](https://taverntesting.github.io/) (*REST API*)

## NOTES
While scratching the surface and as you'll notice in code, there is more testing code than functionality code. That is completely normal, the motivation here is to make sure that the code is robust enough to prevent breaking changes. Also, as a rule of thumb, before pushing any code to production, you must always run the entire test suite. Also, each of the directories here has its own *README* which has specific instructions on running the code there as well as it's test suite.

Additionally, please keep in mind, all this is only meant to run *locally* only. In *production* environment, it'll require more effort such as using static storage like S3 for frontend and any static files that django houses, some kind of WSGI server for django, etc. Also, each part of the system would require different databases for *local*, *test*, *regression*, and *production*.