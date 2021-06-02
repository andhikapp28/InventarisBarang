from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    customer = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, default='NONE')
    address = models.CharField(max_length=200, default='NONE')
    phone = models.CharField(max_length=50, default='NONE')
    image = models.ImageField(default='default.jpg',
                              upload_to='profile_images')

    def __str__(self):
        return f'{self.customer.username}-Profile'