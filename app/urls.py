from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('', home, name='home'),
    path('event/', event_view, name='event'),
    path('delete_event/<event_id>', delete_event, name="delete")
]