from pickle import GET

import requests
from django.http import HttpResponse
from .models import team
from .models import product

# Create your views here.
from django.shortcuts import render
def demo(request):
    obj = team.objects.all()


    return render(request,"index.html",{'result':obj})

