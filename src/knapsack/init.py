import textwrap
from datetime import timedelta

# Create a super user to use the admin site.
from django.contrib.auth.models import User as DjangoUser
from faker import Faker

from knapsack_core.models import User, Question, Knapsack, Tool

fake = Faker()

# Create fake data ...

username = "compsci326"
password = "compsci326"
email = "compsci@326.edu"
adminuser = DjangoUser.objects.create_user(username, email, password)
adminuser.save()
adminuser.is_superuser = True
adminuser.is_staff = True
adminuser.save()
message = f"""
====================================================================
The database has been setup with the following credentials:

  username: {username}
  password: {password}
  email: {email}

You will need to use the username {username} and password {password}
to login to the administrative webapp in Django.

Please visit http://localhost:8080/admin to login to the admin app.
Run the django server with:

  $ python3 manage.py runserver 0.0.0.0:8080"
====================================================================
"""
print(message)
