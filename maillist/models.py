from django.db import models
from django.contrib.auth.models import User

class EmailList(models.Model):
    name = models.CharField(max_length=100)
    subscribers = models.ManyToManyField(User)

    def __str__(self):
        return self.name
