from django.shortcuts import render
from knapsack_core.models import User, Question, Knapsack, Tool

# Create your views here.
def index(request):
  # Use the welcome.html page for now
  return render(request, 'welcome.html', context={})

