from django.db import models

class Contact(models.Model):
    fullname = models.CharField(max_length=50)
    organization = models.CharField(max_length=50)
    position = models.CharField(max_length=20)
    mobile = models.CharField(max_length=15)
    address = models.CharField(max_length=50)

    class Meta:
        ordering = ["-id"]
