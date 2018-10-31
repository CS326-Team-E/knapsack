from django.shortcuts import render
from knapsack_core.models import User, Question, Knapsack, Tool
from django.views import generic

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
