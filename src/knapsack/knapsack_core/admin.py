from django.contrib import admin
from knapsack_core.models import User, Question, Knapsack, Tool

# Register your models here.

# To be used by UserAdmin
class QuestionInline(admin.TabularInline):
	model = Question
	extra = 0
	
# To be used by UserAdmin
class KnapsackInline(admin.TabularInline):
	model = Knapsack
	extra = 0
	
# Register the Admin class with the User model using the decorator
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
	list_display = ("identifier", "last_login", "user_knapsack")
	# This allows to display information about the corresponding questions and knapsack of this User
	inlines = [QuestionInline, KnapsackInline]
	
# Register the Admin class with the Question model using the decorator
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
	list_display = ("question", "username")

admin.site.register(Knapsack)
admin.site.register(Tool)
	