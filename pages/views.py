from django.shortcuts import render
from django.template import loader
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.

def index(request):
	return render(request, 'pages/index.html')



def about(request):
	return render(request,'pages/about.html')


	