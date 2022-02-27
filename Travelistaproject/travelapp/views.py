from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def travel(request):
    return render(request,'travel.html')
