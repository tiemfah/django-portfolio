from django.db import models
from django.utils import timezone

# Create your models here.
class Message(models.Model):
    email = models.CharField(max_length=200)
    message = models.CharField(max_length=200)
    sent_date = models.DateTimeField('date sent', default=timezone.now)

    def __str__(self):
        return f'{self.email}:{self.message}'