from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'recommender.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^query/(?P<uid>[0-9]+)/(?P<mid>[0-9]+)', views.query, name='query'),
    # NOTE The following line handles if the two arguments are not valid input
    # e.g. input a string etc.
    url(r'^get_movie/(?P<uid>[0-9]+)', views.get_movie, name='get_movie'),
    url(r'^get_movie/*', views.error_movie, name='error_movie'),
    url(r'^query/*', views.error, name='error'),
    url(r'', views.index, name='index'),
]
