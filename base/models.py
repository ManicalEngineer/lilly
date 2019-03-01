from django.db import models

# Create your models here.
class Service(models.Model):
    UNIT_CHOICES = (
        ('day', 'day'),
        ('week', 'week'),
        ('visit', 'visit'),
    )
    name = models.CharField(max_length=60)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    unit = models.CharField(choices=UNIT_CHOICES, max_length=30, default='')

class Information(models.Model):
    about = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=13)
    facebook = models.CharField(max_length=100, default='none')
    instagram = models.CharField(max_length=100, default='none')
    twitter = models.CharField(max_length=100, default='none')
