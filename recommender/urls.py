from django.conf.urls import include, url
from django.contrib import admin
from rec import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'recommender.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^rec/', include('rec.urls')),
]
