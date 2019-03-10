from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete =models.CASCADE)
    name = models.CharField(max_length=255, null=False)
    address = models.CharField(max_length=255, null=False)
    phone = models.IntegerField(null=False)
    email = models.CharField(max_length=255, null=False)
    edad = models.IntegerField(null=False)

    class Meta:
        db_table = "Profile"