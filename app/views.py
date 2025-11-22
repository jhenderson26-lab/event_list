from django.shortcuts import render
from . import forms

# Create your views here.

def home(request):
    event = forms.eventForm()
    context = {'event': event}
    return render(request, 'base.html', context)