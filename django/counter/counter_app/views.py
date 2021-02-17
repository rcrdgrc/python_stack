from django.shortcuts import render, HttpResponse, redirect


def index(request):
    if 'counter' in request.session:
        request.session['counter'] = request.session['counter'] + 1
    else:
        request.session['counter'] = 1
    return render(request, "index.html")

def destroy_session(request):
    del request.session['counter']
    return redirect("/")

def plus2(request):
    request.session['counter'] = request.session['counter'] + 2
    return render(request, "index.html")
