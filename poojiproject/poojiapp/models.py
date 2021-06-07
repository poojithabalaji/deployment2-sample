from django.db import models


# Create your models here.
class studentdetails(models.Model):
    first_name = models.CharField(max_length=100)
    sur_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
