# Create a super user to use the admin site.
from django.contrib.auth.models import User as DjangoUser
from faker import Faker

from knapsack_core.models import User, Question, Knapsack, Tool

fake = Faker()

# Create fake data 

# Create Users
users = []
for i in range(1, 50):
  a_identifier = fake.safe_email()
  user = User(identifier=a_identifier)
  user.save()
  users.append(user)

# Create Questions
questions = []
for user in users:
  # Generate a random number of questions for each user
  random_max = fake.random_int(1, 4)
  for i in range(1, random_max):
    a_username = user
    a_question = fake.text(100)
    a_question = a_question[:len(a_question) - 1] + "?"
    a_answer = fake.text(100)
    question = Question(username=a_username, question=a_question, answer=a_answer)
    question.save()
    questions.append(question)

# Create Tools
tools = []
for i in range(1, 10):
  a_identifier = fake.text(40)
  a_path = fake.uri_path(deep=3) 
  a_description = fake.text(200)
  tool = Tool(identifier=a_identifier, path=a_path, description=a_description)
  tool.save()
  tools.append(tool)

# Create Knapsacks
knapsacks = []
for user in users:
  knapsack = Knapsack(owner=user)
  knapsack.save()
  # Add a random number of tools
  random_max = fake.random_int(2, 11)
  for i in range(1, random_max):
    knapsack.tools.add(tools[fake.random_int(0, len(tools)) - 1])
  knapsacks.append(knapsack)

for knapsack in knapsacks:
  user = knapsack.owner
  user.user_knapsack = knapsack
  user.save()

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
