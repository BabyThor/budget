from django.db import models


class Event(models.Model):
    name = models.CharField(null=False, blank=False, max_length=200)
    event_date = models.DateField(null=False, blank=False)
    budget_amount = models.PositiveIntegerField(null=False, blank=False, default=0)
    note = models.CharField(null=True, blank=True, max_length=1000)
