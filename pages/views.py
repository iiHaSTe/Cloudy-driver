
from django.shortcuts import render
from django.http import HttpResponse
from pprint import pprint

def index(req):
    return render(req, 'pages/index.html', {
        'title': '',
        'siteName': 'Cloudy',
        'isHome': True,
        'login': True
    })

def login(req):
    return render(req, 'pages/login.html', {
        'title': 'login',
        'siteName': 'Cloudy'
    })
