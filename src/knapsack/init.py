# Create a super user to use the admin site.
from django.contrib.auth.models import User as DjangoUser
from faker import Faker
from django.utils import timezone
import random

from knapsack_core.models import User, Question, Knapsack
from knapsack_core.models import Tool, ToolRequest, ToolVote

fake = Faker()

# Create Users
users = []
for i in range(0, 50):
    a_identifier = fake.safe_email()
    a_password = fake.password()
    a_last_login = fake.date_time_this_month(
        before_now=True,
        after_now=False,
        tzinfo=timezone.get_default_timezone()
    )
    user = User(identifier=a_identifier,
                password=a_password, last_login=a_last_login)
    user.save()
    users.append(user)

a_identifier = "bigbro@email.com"
a_password = "bigbro"
a_last_login = fake.date_time_this_month(
    before_now=True,
    after_now=False,
    tzinfo=timezone.get_default_timezone()
)
user = User(identifier=a_identifier,
            password=a_password, last_login=a_last_login)
user.save()
users.append(user)


# Create Questions
questions = []
for user in users:
    # Generate a random number of questions for each user
    random_max = fake.random_int(0, 3)
    for i in range(0, random_max):
        a_username = user
        a_question = fake.text(70)
        a_answer = fake.text(40)
        question = Question(username=a_username,
                            question=a_question, answer=a_answer)
        question.save()
        questions.append(question)

# Create Tools
tools = []
for i in range(0, 10):
    a_identifier = fake.text(40)
    a_path = fake.uri_path(deep=3)
    a_description = fake.text(200)
    tool = Tool(identifier=a_identifier, path=a_path,
                description=a_description)
    tool.save()
    tools.append(tool)

# Create Knapsacks
knapsacks = []
for user in users:
    knapsack = Knapsack(owner=user)
    knapsack.save()
    # Add a random number of tools
    random_max = fake.random_int(0, len(tools))
    for i in range(0, random_max):
        knapsack.tools.add(tools[fake.random_int(0, len(tools)) - 1])
    knapsacks.append(knapsack)

for knapsack in knapsacks:
    user = knapsack.owner
    user.user_knapsack = knapsack
    user.save()

# Create ToolRequests
toolrequests = []
for i in range(0, 5):
    tr = ToolRequest(username=random.choice(users))
    tr.title = str.title(fake.text(10))
    tr.request = fake.text(50)
    tr.save()
    toolrequests.append(tr)

# Create votes
for tr in toolrequests:
    available_users = users.copy()
    for i in range(0, random.randint(5, 25)):
        user = random.choice(available_users)
        available_users.remove(user)
        vote = ToolVote(username=user, request=tr)
        vote.save()

username = "admin"
password = "admin"
email = "admin@326.edu"
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

  $ python3 manage.py runserver 0.0.0.0:8080
====================================================================
"""
print(message)
