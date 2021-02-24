from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return redirect("/shows")

def shows(request):
    return HttpResponse('this is the main page')

def edit(request, show_id):
    return HttpResponse('edit this show {show_id}')

def new(request):
    return HttpResponse('this is the main page')

def show(request, show_id):
    return HttpResponse(f'this is the show id {show_id}')

def destroy(request, show_id):
    return redirect("/shows")


# '/<int:x>', defaults={'y': 8})