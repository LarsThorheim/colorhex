from django.db import models
from django.utils import timezone

class Color(models.Model):
    descr = models.CharField(max_length=20)
    hexa = models.CharField(max_length=7)
    created_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.save()

    def __str__(self):
        return self.descr

