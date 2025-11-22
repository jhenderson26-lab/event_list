from django.db import models

# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=200)
    set_date = models.PositiveSmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    