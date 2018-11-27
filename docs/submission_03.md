# Overview
Knapsack is a platform that provides college students modular applications
that will improve their campus experience, called "knapsack tools". As more
tools get developed, knapsack users will be able to add more knapsack tools
to their collection, i.e. their knapsack. Knapsack users will also be able
to submit suggestions for new knapsack tools which the community can then
vote on.

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
* Problem: deciding how to add login/logout functionality to our existing
User model
* Success: creating a one-to-one mapping between our existing User model
 and Django's built-in user model
* Problem: figuring out how to customized views for an authenticated user
* Success: learning the right query to use to get a user's knapsack and
 then display the knapsack tools as part of a customized view

# Team Choice
For the final submission, we would like to create at least one new Knapsack
tool and connect it to the library/store page. Another task we would like
to complete is implementing sorting functionality for the library/store and
divide the library section from the store section.
