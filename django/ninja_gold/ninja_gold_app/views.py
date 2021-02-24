from django.shortcuts import render, redirect, HttpResponse
import random


def index(request):
    request.session['activities'] = []
    request.session['score'] = 0
    return render(request, "index.html")


def money(request):
    request.session['num'] = random.randint(-20, 20)

    if request.POST['which_form'] == 'farm':
        request.session['score'] = request.session['score'] +  request.session['num'] 
        activity = [f"Earned {request.session['num']} gold from Farm!", '1'] if request.session['num'] >= 0 else  [f"Lost {request.session['num']} gold from Farm, ...Ouch!", '2'] 
        request.session['activities'].append(activity)
        request.session.save()
    elif request.POST['which_form'] == 'cave':
        request.session['score'] = request.session['score'] +  request.session['num'] 
        activity = [f"Earned {request.session['num']} gold from Cave!", '1'] if request.session['num'] >= 0 else  [f"Lost {request.session['num']} gold from Cave, ...Ouch!", '2'] 
        request.session['activities'].append(activity)
        request.session.save()
    elif request.POST['which_form'] == 'home':
        request.session['score'] = request.session['score'] +  request.session['num'] 
        activity = [f"Earned {request.session['num']} gold from Home!", '1'] if request.session['num'] >= 0 else  [f"Lost {request.session['num']} gold from Home, ...Ouch!", '2'] 
        request.session['activities'].append(activity)
        request.session.save()
    elif request.POST['which_form'] == 'casino':
        request.session['score'] = request.session['score'] +  request.session['num'] 
        activity = [f"Earned {request.session['num']} gold from Casino!", '1'] if request.session['num'] >= 0 else  [f"Lost {request.session['num']} gold from Casino, ...Ouch!", '2'] 
        request.session['activities'].append(activity)
        request.session.save()


    return render(request, "index.html")
    # return HttpResponse("this is the equivalent of @app.route('/')!")


# def index(request):
#     request.session['num'] = random.randint(1, 100)

#     context = {
#         "highLow": "neither"
#     }

#     return render(request, "index.html", context)


# def result(request):
#     guess = request.POST['answer']
#     numberToGuess = request.session['num']
#     highLow = "neither"

#     print(guess, numberToGuess)
#     if int(guess) == numberToGuess:
#         highLow = "winner"
#     elif int(guess) > numberToGuess:
#         highLow = "high"
#     else:
#         highLow = "low"

#     context = {
#         'highLow': highLow
#     }

#     return render(request, "index.html", context)
