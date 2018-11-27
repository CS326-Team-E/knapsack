from knapsack_core.models import User, Question, Knapsack, Tool, ToolRequest, ToolVote
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.shortcuts import render, redirect, get_object_or_404
from django.template import Context, loader
from django.http import HttpResponse
from django.urls import reverse_lazy

# Create your views here.


def index(request):
    # Use the welcome.html page for now
    return render(request, 'welcome.html', context={})


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class MapView(generic.TemplateView):
    template_name = "map_w_toolbar.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            userknap = Knapsack.objects.filter(owner__identifier=self.request.user.email).first()
            print(userknap.tools.all())
            context['tool_list'] = userknap.tools.all()
        else:
            pass
        # context['tool_list'] = Knapsack.objects.all()
        # print(len(Tool.objects.all()))
        return context


def request_component(request):
    requests = ToolRequest.objects.all()
    for tr in requests:
        tvs = ToolVote.objects.filter(request_id=tr.id)
        tr.votes = len(tvs)
        tr.voted = request.user.id in [tv.username.id for tv in tvs]
        tr.votable = request.user.is_authenticated and not tr.voted
        tr.button = 'disabled'
        tr.owner = request.user.id == tr.username.id
        if tr.voted:
            tr.button = 'active'
        elif tr.votable:
            tr.button = ''
    requests = sorted(list(requests), key=lambda r: r.votes, reverse=True)
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


def vote_component(request, request_id):
    tr = get_object_or_404(ToolRequest, id=request_id)
    user = get_object_or_404(User, id=request.user.id)
    try:
        ToolVote.objects.get(username=user, request=tr).delete()
    except ToolVote.DoesNotExist:
        ToolVote.objects.create(username=user, request=tr)
    return redirect('request')


def new_component(request):
    print(request.POST)
    user = get_object_or_404(User, id=request.user.id)
    ToolRequest.objects.create(username=user, title=request.POST.get(
        'title', ''), request=request.POST.get('description', ''))
    return redirect('request')


def remove_component(request, request_id):
    tr = get_object_or_404(ToolRequest, id=request_id)
    user = get_object_or_404(User, id=request.user.id)
    if user == tr.username:
        tr.delete()
    return redirect('request')
