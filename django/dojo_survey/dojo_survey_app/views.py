from django.shortcuts import render, HttpResponse, redirect


def index(request):
    return render(request, "index.html")


def result(request):
    name_from_form = request.POST['name']
    location = request.POST['location']
    comments = request.POST['comments']
    context = {
        "name_on_template": name_from_form,
        "location": location,
        "comments": comments,
    }
    return render(request, "result.html", context)
