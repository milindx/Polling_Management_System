	
from django.urls import path

from . import views as pages_views

urlpatterns = [
	path('', pages_views.index, name ='index'),
	path('about',pages_views.about,name="pages"),
]
