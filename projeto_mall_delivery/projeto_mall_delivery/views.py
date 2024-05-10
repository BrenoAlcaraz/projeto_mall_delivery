# projeto_mall_delivery/views.py

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

def home(request):
    return render(request, 'home.html')
