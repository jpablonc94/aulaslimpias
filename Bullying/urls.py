"""Bullying URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from reports.views import HomeView, CreateView #AnonymousView, HelpView, ExperienceView, ContactoView
from users.views import LoginView, LogoutView, SigninView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view(), name='home'),

    # Reports URLs
    url(r'^new$', CreateView.as_view(), name='create_report'),
   # url(r'^anonimato$', AnonymousView.as_view(), name='anonimato'),
   # url(r'^help$', HelpView.as_view(), name='ayuda'),
   # url(r'^experiencias$', ExperienceView.as_view(), name='experiencias'),
   # url(r'^contacto$', ContactoView.as_view(), name='contancto'),


    # Users URLs
    url(r'^registro$', SigninView.as_view(), name='new_user'),
    url(r'^login$', LoginView.as_view(), name='users_login'),
    url(r'^logout$', LogoutView.as_view(), name='users_logout'),
]
