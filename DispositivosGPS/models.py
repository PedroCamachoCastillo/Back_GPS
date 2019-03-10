from django.db import models
from Unidades.models import Unidades

# Create your models h
class DispositivosGPS(models.Model):
    unity = models.ForeignKey(Unidades, on_delete =models.CASCADE)
    name_model = models.CharField(max_length=255, null=False)
    brand = models.CharField(max_length=255, null=False)
    serial = models.IntegerField(null=False)

    class Meta:
        db_table = "DispositivosGPS"