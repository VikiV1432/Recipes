from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE, related_name='profile')
    avatar=models.ImageField(upload_to="accounts/", blank=True, null=True)
    bio=models.TextField(max_length=500, blank=True, null=True)
    birthday=models.DateField(null=True, blank=True)
    location=models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return f"{self.user.username}'s profile"

