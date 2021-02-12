from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
# Create your views here.
def root(request):  
    return redirect("/blog")

def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")

def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

def create(request):
    return redirect("/")

def show(request, number):
    return HttpResponse(f"placeholder to display blog number: {str(number)}")

def edit(request, number):
    return HttpResponse(f"placeholder to edit blog {str(number)}")

def destroy(request, number):
    return redirect("/blog")

def blogs(request):
    res = {"title": "My First Blog", "content": "Lorem ipusm, and other stuff that goes here"}
    return JsonResponse(res)
