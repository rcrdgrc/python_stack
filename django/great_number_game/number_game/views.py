from django.shortcuts import render, HttpResponse
import random


def index(request):
    request.session['num'] = random.randint(1, 100)

    context = {
        "highLow": "neither"
    }

    return render(request, "index.html", context)


def result(request):
    guess = request.POST['answer']
    numberToGuess = request.session['num']
    highLow = "neither"

    print(guess, numberToGuess)
    if int(guess) == numberToGuess:
        highLow = "winner"
    elif int(guess) > numberToGuess:
        highLow = "high"
    else:
        highLow = "low"

    context = {
        'highLow': highLow
    }

    return render(request, "index.html", context)

# def destroy_session(request):
#     del request.session['counter']
#     return redirect("/")

# def plus2(request):
#     request.session['counter'] = request.session['counter'] + 2
#     return render(request, "index.html")
