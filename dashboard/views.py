from django.shortcuts import render
from django.http import HttpResponse
from .models import Review
import csv
# Create your views here.

def index(request):
    

    return HttpResponse("VIEWS HERE")