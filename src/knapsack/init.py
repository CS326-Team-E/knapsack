# Create a super user to use the admin site.
from django.contrib.auth.models import User as DjangoUser
from faker import Faker
from django.utils import timezone
import random

from knapsack_core.models import User, Question, Knapsack
from knapsack_core.models import Tool, ToolRequest, ToolVote

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import Group
fake = Faker()

# Create user Group
new_group, created = Group.objects.get_or_create(name='users')
# Create Users
users = []
print("Users")
for i in range(0, 50):
    a_identifier = fake.safe_email()
    a_password = fake.password()
    a_last_login = fake.date_time_this_month(
        before_now=True,
        after_now=False,
        tzinfo=timezone.get_default_timezone()
    )
    djangoUser = DjangoUser.objects.create_user(
        a_identifier, a_identifier, a_password)
    group = Group.objects.get(name='users')
    djangoUser.groups.add(group)
    users.append(User.objects.get(mirrored_user=djangoUser))

test_username = "bigbro"
test_email = "bigbro@email.com"
test_password = "bigbro"
user = DjangoUser.objects.create_user(test_username, test_email, test_password)
a_identifier = "bigbro@email.com"
a_password = "bigbro"
a_last_login = fake.date_time_this_month(
    before_now=True,
    after_now=False,
    tzinfo=timezone.get_default_timezone()
)
user = DjangoUser.objects.create_user(a_identifier, a_identifier, a_password)
users.append(User.objects.get(mirrored_user=user))

# Create Questions
print("Questions")
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
print("Tools")
for i in range(0, 10):
    a_identifier = fake.text(40)
    a_description = fake.text(200)
    lead = fake.text(75)
    a_htmls = []
    a_htmls.append(f"""
        <div class="py-5 bg-light component">
            <div class="container">
                <div class="row">
                    <div class="col-md-4">
                        <h2 class="text-center mt-2">{a_identifier}</h2>
                    </div>
                    <div class="col-md-8 pl-5">
                        <p class="lead">{lead}</p>
                        <p>{a_description}</p>
                    </div>
                </div>
            </div>
        </div>
    """)
    a_htmls.append(f"""
        <link href="//netdna.bootstrapcdn.com/twitter-bootstrap/2.3.2/css/bootstrap-combined.min.css" rel="stylesheet" id="bootstrap-css">
        <script src="//netdna.bootstrapcdn.com/twitter-bootstrap/2.3.2/js/bootstrap.min.js"></script>
        <script src="//code.jquery.com/jquery-1.11.1.min.js"></script>

        <div class="container">
            <div class="row">
                <div class="span12">
                    <table class="table-condensed table-bordered table-striped">
                        <thead>
                            <tr>
                              <th colspan="7">
                                <span class="btn-group">
                                    <a class="btn"><i class="icon-chevron-left"></i></a>
                                    <a class="btn active">February 2012</a>
                                    <a class="btn"><i class="icon-chevron-right"></i></a>
                                </span>
                              </th>
                            </tr>
                            <tr>
                                <th>Su</th>
                                <th>Mo</th>
                                <th>Tu</th>
                                <th>We</th>
                                <th>Th</th>
                                <th>Fr</th>
                                <th>Sa</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td class="muted">29</td>
                                <td class="muted">30</td>
                                <td class="muted">31</td>
                                <td>1</td>
                                <td>2</td>
                                <td>3</td>
                                <td>4</td>
                            </tr>
                            <tr>
                                <td>5</td>
                                <td>6</td>
                                <td>7</td>
                                <td>8</td>
                                <td>9</td>
                                <td>10</td>
                                <td>11</td>
                            </tr>
                            <tr>
                                <td>12</td>
                                <td>13</td>
                                <td>14</td>
                                <td>15</td>
                                <td>16</td>
                                <td>17</td>
                                <td>18</td>
                            </tr>
                            <tr>
                                <td>19</td>
                                <td class="btn-primary"><strong>20</strong></td>
                                <td>21</td>
                                <td>22</td>
                                <td>23</td>
                                <td>24</td>
                                <td>25</td>
                            </tr>
                            <tr>
                                <td>26</td>
                                <td>27</td>
                                <td>28</td>
                                <td>29</td>
                                <td class="muted">1</td>
                                <td class="muted">2</td>
                                <td class="muted">3</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    """)
    coorx = random.uniform(42.37, 42.47)
    coory = random.uniform(-72.53, -72.51)
    tool = Tool(identifier=a_identifier, html=random.choice(a_htmls),
                description=a_description, location_x=coorx, location_y=coory)
    tool.save()
    tools.append(tool)

# Create calendar tool
calendar_id = "Calendar"
calendar_desc = "This is a fake calendar"
calendar_x = random.uniform(42.37, 42.47)
calendar_y = random.uniform(-72.53, -72.51)
calendar_html = f"""
        <link href="//netdna.bootstrapcdn.com/twitter-bootstrap/2.3.2/css/bootstrap-combined.min.css" rel="stylesheet" id="bootstrap-css">
        <script src="//netdna.bootstrapcdn.com/twitter-bootstrap/2.3.2/js/bootstrap.min.js"></script>
        <script src="//code.jquery.com/jquery-1.11.1.min.js"></script>

        <div class="container">
            <div class="row">
                <div class="span12">
                    <table class="table-condensed table-bordered table-striped">
                        <thead>
                            <tr>
                              <th colspan="7">
                                <span class="btn-group">
                                    <a class="btn"><i class="icon-chevron-left"></i></a>
                                    <a class="btn active">February 2012</a>
                                    <a class="btn"><i class="icon-chevron-right"></i></a>
                                </span>
                              </th>
                            </tr>
                            <tr>
                                <th>Su</th>
                                <th>Mo</th>
                                <th>Tu</th>
                                <th>We</th>
                                <th>Th</th>
                                <th>Fr</th>
                                <th>Sa</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td class="muted">29</td>
                                <td class="muted">30</td>
                                <td class="muted">31</td>
                                <td>1</td>
                                <td>2</td>
                                <td>3</td>
                                <td>4</td>
                            </tr>
                            <tr>
                                <td>5</td>
                                <td>6</td>
                                <td>7</td>
                                <td>8</td>
                                <td>9</td>
                                <td>10</td>
                                <td>11</td>
                            </tr>
                            <tr>
                                <td>12</td>
                                <td>13</td>
                                <td>14</td>
                                <td>15</td>
                                <td>16</td>
                                <td>17</td>
                                <td>18</td>
                            </tr>
                            <tr>
                                <td>19</td>
                                <td class="btn-primary"><strong>20</strong></td>
                                <td>21</td>
                                <td>22</td>
                                <td>23</td>
                                <td>24</td>
                                <td>25</td>
                            </tr>
                            <tr>
                                <td>26</td>
                                <td>27</td>
                                <td>28</td>
                                <td>29</td>
                                <td class="muted">1</td>
                                <td class="muted">2</td>
                                <td class="muted">3</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    """
calendar_tool = Tool(identifier=calendar_id, html=calendar_html,
                description=calendar_desc, location_x=calendar_x,
                location_y=calendar_y)
calendar_tool.save()
tools.append(calendar_tool)

# Create Knapsacks
knapsacks = []
print("Knapsacks")
for user in users:
    knapsack = Knapsack(owner=user)
    knapsack.save()
    # Add a random number of tools
    random_max = fake.random_int(3, len(tools))
    for i in range(0, random_max):
        knapsack.tools.add(tools[fake.random_int(0, len(tools)) - 1])
        knapsack.tools.add(calendar_tool)
    knapsacks.append(knapsack)

for knapsack in knapsacks:
    user = knapsack.owner
    user.user_knapsack = knapsack
    user.save()

# Create ToolRequests
print("Requests")
toolrequests = []
for i in range(0, 5):
    tr = ToolRequest(username=random.choice(users))
    tr.title = str.title(fake.text(10))
    tr.request = fake.text(50)
    tr.save()
    toolrequests.append(tr)

# Create votes
print("Votes")
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
