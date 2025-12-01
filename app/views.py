from django.shortcuts import render, redirect
from . import forms
from . import models
from datetime import timedelta, datetime
from datetime import date

# Create your views here.
def check_event(day):
    int_date = int((f'{day.event_date.year}' + f'{day.event_date.month}' + f'{day.event_date.day}'))
    tday = date.today()
    int_today = int((f'{tday.year}' + f'{tday.month}' + f'{tday.day}'))
    if int_date > int_today:
        day.save()
    else:
        day.delete()
    
def home(request):
    event = forms.EventForm()
    event_list = models.Event.objects.all()
    list_order = models.Event.objects.all().order_by("event_date")
    for events in event_list:
        if events.until_event == None:
            events.delete()
        check_event(events)
    context = {'event': event, 'text': list_order}
    return render(request, 'base.html', context)

def event_view(request):
    if request.method == 'POST':
        form = forms.EventForm(request.POST)
        if form.is_valid():
            form.save()
            for day in models.Event.objects.all():
                change_date = day.created_at + timedelta(days=(day.set_date ))
                day.event_date = change_date
                check_event(day)
        return redirect('home')

 
def delete_event(request, event_id):
    event = models.Event.objects.get(id=event_id)
    event.delete()
    return redirect('home')
