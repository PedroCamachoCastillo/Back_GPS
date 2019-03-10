from django.db import models
from Profile.models import Profile

# Create your models here.
class Unidades(models.Model):
    profile = models.ForeignKey(Profile, on_delete =models.CASCADE)
    plate = models.CharField(max_length=255, null=False)
    brand = models.CharField(max_length=255, null=False)
    color = models.CharField(max_length=255, null=False)

    class Meta:
        db_table = "Unidades"