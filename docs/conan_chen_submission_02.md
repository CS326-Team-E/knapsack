Conan Chen

I set up the skeleton website using the django-admin and manage.py commands. I
also contributed to writing the data models. Specifically, I wrote the Question
data model and some of the class methods for the other data models.

I also set up the admin site and the creation of fake data. I wrote the init.sh
script (using the code from the examples in class) and most of the init.py
script. Based off the examples in class, I used Faker to generate fake data for
the User, Question, Tool, and Knapsack data models and used Django to add them
to the database.

Lastly, I wrote the template for the library page, library.html, which displays
the tools from a user's knapsack in a flexible grid format, using the Django
templating language and Bootstrap. I also implemented a searchbar for this page
and added an example tool (just on the frontend) which, through the launch
button on its Bootstrap card, links to a page for that tool. Jacob had written
the html page for this before, so I turned it into a Django template which extends
our base template. For these pages I wrote the necessary view functions and
urls.
