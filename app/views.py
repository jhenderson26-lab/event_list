from django.shortcuts import render, redirect
from . import forms
from . import models
from datetime import timedelta

# Create your views here.

def home(request):
    event = forms.EventForm()
    event_list = models.Event.objects.all()
    for events in event_list:
        if events.until_event <= 0:
            events.delete()
    context = {'event': event, 'text': event_list}
    return render(request, 'base.html', context)

def event_view(request):
    if request.method == 'POST':
        form = forms.EventForm(request.POST)
        if form.is_valid():
            form.save()
            for day in models.Event.objects.all():
                change_date = day.created_at + timedelta(days=(day.set_date -1))
                day.event_date = change_date
                day.save()
            
        return redirect('home')

def delete_event(request, event_id):
    event = models.Event.objects.get(id=event_id)
    event.delete()
    return redirect('home')
