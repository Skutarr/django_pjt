from django.shortcuts import render
from django.http import HttpResponse
from django import template
import os


# Create your views here.

def home(request):

    return render(request, "templates/index.html")

