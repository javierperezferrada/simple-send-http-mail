from django.conf.urls import include, url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.sendmail ,name='sendmail'),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),

]
