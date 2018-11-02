from knapsack_core.models import Question, Knapsack, Tool, ToolRequest, ToolVote
from knapsack_core.models import User
from django.views import generic
from django.shortcuts import render

# Create your views here.


def index(request):
    # Use the welcome.html page for now
    return render(request, 'welcome.html', context={})


class MapView(generic.TemplateView):
    template_name = "map_w_toolbar.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['tool_list'] = Tool.objects.all()
        print(len(Tool.objects.all()))
        return context


def request_component(request):
    requests = ToolRequest.objects.all()
    for req in requests:
        req.votes = len(ToolVote.objects.filter(request_id=req.id))
        req.voted = request.user.id not in [
            tv.username.id for tv in ToolVote.objects.all()]
        req.votable = request.user.is_authenticated and not req.voted
    return render(request, 'request_component.html', context={
        'requests': requests
    })

class LibraryView(generic.TemplateView):
    template_name = 'library.html'

    # We do not have user authentication yet, so just use the first test users'
    # knapsack
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['knapsack'] = Knapsack.objects.first()
        return context
