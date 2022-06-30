from django.urls import path
from . import views

urlpatterns = [
    path("" , views.index, name= 'index'),
    path("cache/" , views.cache, name= 'cache'),
    path("search/" , views.search, name= 'search')
]
