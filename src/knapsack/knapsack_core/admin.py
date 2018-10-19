from django.contrib import admin
from knapsack_core.models import User, Question, Knapsack, Tool

# Register your models here.
admin.site.register(User)
admin.site.register(Question)
admin.site.register(Knapsack)
admin.site.register(Tool)
