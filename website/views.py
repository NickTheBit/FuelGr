from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.

def index(request):
    return HttpResponse("<h1>Welcome to Mailing System Python Django App</h1>")


class IndexView(TemplateView):
    template_name = "index.html"
    