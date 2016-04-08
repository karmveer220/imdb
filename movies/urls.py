from django.conf.urls import patterns, include, url
from movies import views

urlpatterns = patterns('',
    (r'^all', views.all_movies,{},'all_movies'),
    (r'^search', views.search_movies,{},'search_movies'),
)
