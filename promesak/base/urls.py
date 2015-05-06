"""promesak URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from promesak.base import views as baseviews
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^party/$',
        RedirectView.as_view(pattern_name='index')),
    url(r'^party/(?P<slug>[-\w]+)?',
        baseviews.party_view, name='party_view'),
    url(r'^promise/$',
        RedirectView.as_view(pattern_name='index')),
    url(r'^promise/(?P<slug>[-\w]+)?',
        baseviews.promise_view, name='promise_view'),
]
