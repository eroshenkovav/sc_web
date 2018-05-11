from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
from django.template import RequestContext
from datetime import datetime
from django.template import loader
#from .models import Project
# Create your views here.

def home(request):
    #"""Renders the home page."""
    #assert isinstance(request, HttpRequest)
    #return render(
    #    request,
    #    'app/index.html',
    #    {
    #        'title':'Home Page',
    #        'year':datetime.now().year,
    #    }
    #)
    project_list = []
    template = loader.get_template('app/index.html')
    context = {
        'project_list': project_list,
    }
    return HttpResponse(template.render(context, request))