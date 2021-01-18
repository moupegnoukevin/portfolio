from django.shortcuts import render
from .models import Projet

def index(request):
    projet=Projet.objects.all()
    return render(request,'index.html',{'projet':projet})
