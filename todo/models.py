from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=True)
    when_to_do = models.DateField(null=False)
    email = models.EmailField(max_length=200, null=False)
    created = models.DateTimeField(auto_now_add=True, null=True)
    completed = models.BooleanField(default=False, null=True)

    def __str__(self):
        return self.title