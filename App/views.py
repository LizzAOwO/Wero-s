from django.shortcuts import render
from django.http import JsonResponse
import json
from django.core import serializers
from App.models import Alimento

# Create your views here.
def home(request):
    data = serializers.serialize("json", list(Alimento.objects.all()))
    return render(request,"index.html",{"data":data})