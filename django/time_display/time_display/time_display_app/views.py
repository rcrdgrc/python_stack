from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, localtime, strftime

def root(request):
    return redirect("/time_display")    

def index(request):
    context = {
        "date": strftime("%B %d, %Y", localtime()),
        "time": strftime("%H:%M %p", gmtime())
    }
    return render(request, "index.html", context)
