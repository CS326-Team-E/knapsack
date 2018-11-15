from django.contrib import admin
from knapsack_core.models import User, Question, Knapsack
from knapsack_core.models import Tool, ToolRequest, ToolVote

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
    # This allows to display information about the corresponding questions and
    # knapsack of this User
    inlines = [QuestionInline, KnapsackInline]


# Register the Admin class with the Question model using the decorator
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("question", "username")


# Register the other models normally
admin.site.register(Knapsack)
admin.site.register(Tool)


@admin.register(ToolRequest)
class ToolRequestAdmin(admin.ModelAdmin):
    list_display = ('username', 'title', 'request', 'get_votes')

    def get_votes(self, obj):
        return len(ToolVote.objects.filter(request_id=obj.id))
