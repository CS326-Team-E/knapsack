from knapsack_core.models import User, Question, Knapsack, Tool, ToolRequest, ToolVote
from django.views import generic
from django.shortcuts import render
from django.template import Context, loader
from django.http import HttpResponse

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
    req.voted = request.user.id in [tv.username.id for tv in ToolVote.objects.all()]
    req.votable = request.user.is_authenticated and not req.voted
    req.button = 'disabled'
    if req.voted:
      req.button = 'active'
    elif req.votable:
      req.button = ''
  requests = sorted( list(requests), key=lambda r:r.votes, reverse=True)
  return render(request, 'request_component.html', context={
    'requests': requests
  })
  
class LibraryView(generic.TemplateView):
    template_name = 'library.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['knapsack'] = Knapsack.objects.first()
        query = self.request.GET.get('q')
        if query:
            context['query'] = self.request.GET['q']
        else:
            context['query'] = ''
        return context

def single_component(request):
    return render(request, 'single_component.html', context={})
    