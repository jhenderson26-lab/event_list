from django.shortcuts import render, redirect
from . import forms
from . import models

# Create your views here.

def home(request):
    event = forms.EventForm()
    context = {'event': event}
    return render(request, 'base.html', context)

def event_view(request):
    if request.method == 'POST':
        form = forms.EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event')
    event_list = models.Event.objects.all()
    context = {'text': event_list}
    return render(request, 'other.html', context)

def delete_event(request, event_id):
    event = models.Event.objects.get(id=event_id)
    event.delete()
    return redirect('event')
 