from django.shortcuts import render
from knapsack_core.models import User, Question, Knapsack, Tool, ToolRequest, ToolVote

# Create your views here.
def index(request):
  # Use the welcome.html page for now
  return render(request, 'welcome.html', context={})

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