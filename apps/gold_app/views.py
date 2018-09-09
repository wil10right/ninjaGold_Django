from django.shortcuts import render, redirect
from . import views
from time import strftime
import datetime, random

def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'action' not in request.session:
        request.session['actions'] = []
    return render(request, "index.html")

def processMoney(request):

    now = str(datetime.datetime.now())
    if request.POST['building'] == 'farm':
        request.session['num'] = random.randint(10,20)
        request.session['gold'] += request.session['num']
        request.session['actions'].insert(0, "<p style='color: green'>You found "+str(request.session['num'])+" gold in your Farm.  "+now+"</p>")

    if request.POST['building'] == 'cave':
        request.session['num'] = random.randint(5,10)
        request.session['gold'] += request.session['num']
        request.session['actions'].insert(0, "<p style='color: green'>You found "+str(request.session['num'])+" gold in a dank Cave.  "+now+"</p>")

    if request.POST['building'] == 'house':
        request.session['num'] = random.randint(2,5)
        request.session['gold'] += request.session['num']
        request.session['actions'].insert(0, "<p style='color: green'>You found "+str(request.session['num'])+" gold in your House.  "+now+"</p>")

    if request.POST['building'] == 'casinos':
        request.session['num'] = random.randint(-50,50)
        if request.session['num'] > 0:
            request.session['gold'] += request.session['num']
            request.session['actions'].insert(0, "<p style='color: green'>You WON "+str(request.session['num'])+" at the Casino.  "+now+"</p>")
        if request.session['num'] <= 0:
            request.session['gold'] += request.session['num']
            request.session['actions'].insert(0, "<p style='color: red'>You LOST "+str(request.session['num']*-1)+" at the Casino.  "+now+"</p>")

    # print(request.session['actions'])

    return redirect('/me_gold')

def meGold(request):
    return render(request, 'index.html')

def reset(request):
    request.session.clear()
    return redirect('/')
# Create your views here.
