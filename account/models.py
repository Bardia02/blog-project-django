from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    usere1=models.OneToOneField(User,on_delete=models.CASCADE)
    fathers_name=models.CharField(max_length=50)
    code_meli=models.CharField(max_length=20)
    image=models.ImageField(upload_to="profile/images")

    def __str__(self):
        return self.usere1.username