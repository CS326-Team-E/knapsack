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
    req.voted = request.user.id not in [tv.username.id for tv in ToolVote.objects.all()]
    req.votable = request.user.is_authenticated and not req.voted
  return render(request, 'request_component.html', context={
    'requests': requests
  })