from django.shortcuts import render, redirect
from dojo_ninja_app.models import *

def index(request):
    context = {"dojos": Dojo.objects.all()}	
    return render(request, "index.html", context)

def addDojo(request):
    first = request.POST['name']
    city = request.POST['city']
    state = request.POST['state']

    Dojo.objects.create(name=first, city=city, state=state)

    return redirect("/")

def addNinja(request):
    first = request.POST['first_name']
    last = request.POST['last_name']
    dojo = Dojo.objects.get(name=request.POST['dojo'])
   
    Ninja.objects.create(first_name=first, last_name=last, dojo=dojo)

    return redirect("/")