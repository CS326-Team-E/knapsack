# Overview

# Team Members
* Jingshu Meng
* Zhihan Ying
* Conan Chen
* William He
* Jacob Goldman

# Video Link

# Design Overview
To enable login/logout and interaction functionality for our web
application, we created a one-to-one mapping between our User model and
Django's built-in user model. This allows the User model to be associated
with Django's built-in user model and for class variables belonging to the
User model to be mapped to Django's built-in user model.  To set up our
authentication views, we added `path('accounts/',
include('django.contrib.auth.urls'))` to our `urlpatterns` in urls.py and
added the login.html page to our templates directory. The login.html page
uses a form with Django's csrf\_token to provide login functionality. Our
view classes such as MapView and LibraryView can then provide customized
views by accessing the user instance associated with the request and
performing queries on the database.

# Problems/Successes

# Team Choice
