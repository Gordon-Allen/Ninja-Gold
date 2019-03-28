from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string
import random
from time import gmtime, strftime

def index(request):
    if "total" not in request.session or "activity" not in request.session:
        request.session['total'] = 0
        request.session['activity'] = []
    context = {
        'total': request.session['total'],
        'acitivity': request.session['activity'],
    }
    return render(request, 'main_app/index.html', context)

def process_money(request):
    activity = request.session['activity']
    date = strftime("%Y-%m-%d %H:%M %p", gmtime())
    sentence_data = {
        'date': date,
        'building': request.POST['building'],
    }
    if request.method == "POST":
        if request.POST['building'] == 'Farm':
            rand = random.randint(10,20)
            sentence_data['amount'] = rand
            request.session['total'] += rand

        elif request.POST['building'] == 'Cave':
            rand = random.randint(5,10)
            sentence_data['amount'] = rand
            request.session['total'] += rand

        elif request.POST['building'] == 'House':
            rand = random.randint(2,5)
            sentence_data['amount'] = rand
            request.session['total'] += rand

        elif request.POST['building'] == 'Casino':
            rand = random.randint(-50,50)
            sentence_data['amount'] = rand
            request.session['total'] += rand

    activity.append(sentence_data)
    return redirect('/')

def reset (request):
    if request.method == "POST":
        request.session['total'] = 0
        request.session['activity'] = []
    return redirect('/')