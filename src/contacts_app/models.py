from django.conf import settings
from django.db import models
from django.contrib.auth import get_user_model
User=get_user_model()

class Contact(models.Model):
    fullname = models.CharField(max_length=50)
    organization = models.CharField(max_length=50)
    position = models.CharField(max_length=20)
    mobile = models.CharField(max_length=15)
    address = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        ordering = ["-id"]

