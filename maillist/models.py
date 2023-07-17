from django.db import models

class EmailList(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(null=True)

    def __str__(self):
        return self.name
