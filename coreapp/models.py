from django.db import models

# Create your models here.
class add_post(models.Model):
    title = models.CharField(max_length=200)
    desh = models.TextField()
    complete = models.BooleanField(default=False)