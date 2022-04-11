from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Topic(models.Model):
    objects = None
    title = models.CharField(max_length=30)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
