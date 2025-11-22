from django import forms
from .models import Event

class eventForm(forms.ModelForm):
    event_name = forms.CharField(label='Event Name', max_length=100)
    setdate = forms.IntegerField()
    class Meta:
        model = Event
        fields = ['event_name', 'setdate',]    