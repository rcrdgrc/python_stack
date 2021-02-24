from django.shortcuts import render, HttpResponse, redirect
from user_app.models import *


def index(request):
    print(User.objects.count())
    if User.objects.count() == 0:
        context = {
            "user_count": 0
        }
    else:
        context = {
            "all_users": User.objects.all(),
            "user_count": User.objects.count()
        }

    return render(request, "index.html", context)


def submit(request):
    first = request.POST['first']
    last = request.POST['last']
    email = request.POST['email']
    age = request.POST['age']

    User.objects.create(first_name=first, last_name=last, email_address=email,
                        duration=age, created_at="1987-09-25", updated_at="1987-09-25")

    return redirect("/")
